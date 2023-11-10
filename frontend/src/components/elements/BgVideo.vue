<template>
    <video :id="'bg_' + classname" autoplay loop muted>
        <source :src="'src/assets/video/' + video_src + '.mp4'" type="video/mp4">
    </video>
</template>
<script setup>
defineProps({
    video_src: String,
    classname: String
})
</script>
<style>
#bg_singles_featurings_video,
#bg_video_extras {
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
}

#bg_singles_featurings_video {
  filter: hue-rotate(25deg);
}

#bg_video_extras {
  filter: brightness(.7);
}
</style>