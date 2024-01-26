<template>
  <div class="row">
    <div class="col-xl-12">
      <form @submit.prevent="submitForm" @reset="onReset" class="form-horizontal" role="form"
        enctype="multipart/form-data">
        <div class="row">
          <div class="col-xl-6 mt-2">
            <label class="required">Project Name</label> :
            <div>
              <input id="rounded" autocomplete="off" v-model="form.name" type="text" class="form-control" name="name"
                :class="{ 'is-invalid': $v.form.name.$error }" placeholder="Enter the product name" />
              <div v-if="$v.form.name.$error" class="invalid-feedback">
                <span v-if="!$v.form.name.required">The project name must be filled in.</span>
              </div>
            </div>
          </div>
          <div class="col-xl-6 mt-2">
            <label class="required">Start Date</label> :
            <div>
              <b-form-datepicker id="example-datepicker" v-model="form.start_date" class="mb-2" :class="{ 'is-invalid': $v.form.start_date.$error }"></b-form-datepicker>
              <div v-if="$v.form.start_date.$error" class="invalid-feedback">
                <span v-if="!$v.form.start_date.required">The start_date must be filled in</span>
              </div>
            </div>
          </div>
          <div class="col-xl-12 mt-2 form-group">
            <label for="exampleFormControlTextarea1">Description</label>
            <textarea v-model="form.description" class="form-control" id="exampleFormControlTextarea1" rows="3"
              :class="{ 'is-invalid': $v.form.description.$error }" placeholder="Enter product description"></textarea>
            <div v-if="$v.form.description.$error" class="invalid-feedback">
              <span v-if="!$v.form.description.required">The description must be filled in</span>
            </div>
          </div>
        </div>
        <div class="col-xl-12 text-center pt-4 pb-4">
          <b-button variant="primary" class="w-md" type="submit"><i class="uil uil-save mx-1"></i>Simpan</b-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";

export default {
  props: {
    items: {
      type: Object,
      default: () => {
        return {}
      },
    },
  },
  data() {
    return {
      form: {
        name: this.items.name,
        start_date: this.items.start_date,
        description: this.items.description,
      },
    };
  },
  validations: {
    form: {
      name: {
        required
      },
      start_date: {
        required
      },
      description: {
        required
      },
    }
  },
  watch: {
    items: {
      handler: function (val) {
        if (val) {
          this.form.name = val.name
          this.form.start_date = val.start_date
          this.form.description = val.description
        }
      },
      deep: true,
      immediate: true,
    },
  },
  methods: {
    submitForm() {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.submit = true;
        this.$emit('input', this.form)
      }
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.name = null
      this.form.start_date = null
      this.form.description = null
      this.$v.$reset();
    },
  },
  async created() {
  },
  mounted() {
  }
};
</script>
