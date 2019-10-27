<template>
    <div>
        <!-- <a :href="content.file_name.full_path" download> -->
        <a :href="download_url" :download="content.base_name">Download {{ content.base_name }}</a>
        <!-- </a> -->
    </div>
</template>

<script>
export default {
    name: 'downloadButton',
    props: ['content'],
    data() {
        return {
            download_url: ''
        };
    },
    created() {
        console.log(this.content);
        const file_obj = new File([this.content.content], new String(this.content.base_name));
        console.log(file_obj);
        this.download_url = URL.createObjectURL(file_obj);
    }
};
</script>
