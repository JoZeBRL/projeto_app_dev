const fs = require('fs');
const path = require('path');

const envExamplePath = path.join(__dirname, 'Backend', '.env.example');
const envPath = path.join(__dirname, 'Backend', '.env');

if (!fs.existsSync(envPath) && fs.existsSync(envExamplePath)) {
  console.log('Criando Backend/.env a partir do Backend/.env.example...');
  fs.copyFileSync(envExamplePath, envPath);
  console.log('Arquivo Backend/.env criado com sucesso. Por favor, ajuste as variáveis necessárias.');
} else if (fs.existsSync(envPath)) {
  console.log('Arquivo Backend/.env já existe, prosseguindo com inicialização...');
} else {
  console.log('Arquivo Backend/.env.example não encontrado. Verifique os arquivos do projeto.');
}
