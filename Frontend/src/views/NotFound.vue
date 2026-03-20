<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-white dark:bg-black p-6 text-center">
        <h1 class="text-9xl font-black text-gray-100 dark:text-white/5 absolute -z-10 select-none">404</h1>
        <div class="space-y-6">
            <h2 class="text-4xl font-black uppercase tracking-tight dark:text-white">Página Não Encontrada</h2>
            <p class="text-[10px] font-bold uppercase tracking-[0.3em] text-gray-400 max-w-xs mx-auto">
                O conteúdo que você está procurando não existe ou foi movido.
            </p>
            <v-btn to="/dashboard" color="black" dark class="!rounded-full !px-12 !h-14 !font-black !text-xs !tracking-widest">
                Voltar ao Início
            </v-btn>
        </div>
    </div>
</template>
