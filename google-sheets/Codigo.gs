// =====================================================================
// Plataforma Larissa de Campos — recebedor de dados (Sheets + Drive)
// Cole TODO este código no Apps Script da sua planilha
// (na planilha: menu Extensões > Apps Script, apague o que estiver lá e cole isto).
//
// IMPORTANTE: depois de colar, é preciso REIMPLANTAR e AUTORIZAR de novo
// (agora o script também guarda fotos no seu Google Drive). Passo a passo no
// arquivo COMO-CONECTAR.md.
// =====================================================================

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);

    // ---- Caso seja uma FOTO: salva no Google Drive ----
    if (d.tipo === 'foto' && d.imagem) {
      var pasta = pastaDoAluno(d.aluno);
      var nomeArq = carimbar(d.arquivo || ((d.aluno || 'Aluno') + ' - ' + (d.item || 'foto') + '.jpg'));
      var blob = Utilities.newBlob(Utilities.base64Decode(d.imagem), 'image/jpeg', nomeArq);
      var arquivo = pasta.createFile(blob);
      registrar(d.aluno, 'foto', d.item || '', '', 'Foto recebida', arquivo.getUrl());
      return ok();
    }

    // ---- Demais dados (carga, check-in, atividade): vão para a planilha ----
    registrar(d.aluno, d.tipo, d.item, d.valor, d.detalhes, '');
    return ok();

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, erro: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Acrescenta uma linha na aba "Dados" (cria o cabeçalho na primeira vez)
function registrar(aluno, tipo, item, valor, detalhes, link) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Dados') || ss.insertSheet('Dados');
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Data/Hora', 'Aluno', 'Tipo', 'Item', 'Valor', 'Detalhes', 'Foto']);
    sheet.getRange(1, 1, 1, 7).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  sheet.appendRow([ new Date(), aluno || '', tipo || '', item || '', valor || '', detalhes || '', link || '' ]);
}

// Pasta de cada aluno dentro de "Fotos Alunos - Plataforma" no seu Drive
function pastaDoAluno(aluno) {
  var raiz = subpasta(DriveApp.getRootFolder(), 'Fotos Alunos - Plataforma');
  return subpasta(raiz, ((aluno || 'Aluno').trim()) || 'Aluno');
}
function subpasta(pai, nome) {
  var it = pai.getFoldersByName(nome);
  return it.hasNext() ? it.next() : pai.createFolder(nome);
}

// Coloca data e hora no começo do nome do arquivo, pra ficar em ordem
function carimbar(nome) {
  var sel = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd_HH-mm');
  return sel + '  ' + nome;
}

function ok() {
  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

// só pra você testar abrindo o link no navegador
function doGet() {
  return ContentService.createTextOutput('Plataforma Larissa Campos — conexão ativa. Tudo certo!');
}
