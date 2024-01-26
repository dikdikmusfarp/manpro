<template>
  <div>
    <!-- <customer></customer> -->
  </div>
</template>

<script>
// import customer from '~/components/Dashboard/customer'

export default {
  name: 'IndexPage',
  layout: 'base',
  methods: {
    async getListProduct() {
      this.$store.dispatch("project/index", { })
        .then((resp) => {
          this.table.items = resp.data
        })
        .catch((error) => {
        });
    },
  },
  async created() {
    await this.getListProduct();
  },
  // components: {
  //   customer
  // },
}
</script>
