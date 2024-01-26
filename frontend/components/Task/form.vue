<template>
  <div class="row">
    <div class="col-xl-12">
      <form @submit.prevent="submitForm" @reset="onReset" class="form-horizontal" role="form"
        enctype="multipart/form-data">
        <div class="row">
          <div class="col-xl-6 mt-2">
            <label class="required">Task Name</label> :
            <div>
              <input id="rounded" autocomplete="off" v-model="form.name" type="text" class="form-control" name="name"
                :class="{ 'is-invalid': $v.form.name.$error }" placeholder="Enter the task name" />
              <div v-if="$v.form.name.$error" class="invalid-feedback">
                <span v-if="!$v.form.name.required">The task name must be filled in.</span>
              </div>
            </div>
          </div>
          <div class="col-xl-6 mt-2">
            <label class="required">Project</label> :
            <b-form-group id="input-group-1" label-for="input-sekolah">
              <multiselect v-model="form.project_id" :options="optionProject.map((type) => type.id)" :custom-label="(opt) =>
                optionProject.find((x) => x.id == opt)
                  ? optionProject.find((x) => x.id == opt).name
                  : null
                " placeholder="Choose project" :class="{ 'is-invalid': $v.form.project_id.$error }">
              </multiselect>
              <div v-if="$v.form.project_id.$error" class="invalid-feedback">
                <span v-if="!$v.form.project_id.required">You have to choose one</span>
              </div>
            </b-form-group>
          </div>
          <div class="col-xl-6 mt-2">
            <label class="required">Status</label> :
            <b-form-group id="input-group-1" label-for="input-sekolah">
              <multiselect v-model="form.status_id" :options="optionStatus.map((type) => type.id)" :custom-label="(opt) =>
                optionStatus.find((x) => x.id == opt)
                  ? optionStatus.find((x) => x.id == opt).name
                  : null
                " placeholder="Choose status" :class="{ 'is-invalid': $v.form.status_id.$error }">
              </multiselect>
              <div v-if="$v.form.status_id.$error" class="invalid-feedback">
                <span v-if="!$v.form.status_id.required">You have to choose one</span>
              </div>
            </b-form-group>
          </div>
          <div class="col-xl-6 mt-2">
            <label class="required">Time</label> :
            <div>
              <input id="rounded" autocomplete="off" v-model="form.time" type="number" class="form-control" name="time"
                :class="{ 'is-invalid': $v.form.time.$error }" placeholder="Enter product time quantity" />
              <div v-if="$v.form.time.$error" class="invalid-feedback">
                <span v-if="!$v.form.time.required">The time must be filled in</span>
              </div>
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
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";

export default {
  components: {
    Multiselect,
  },
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
        time: this.items.time,
        project_id: this.items.project_id,
        status_id: this.items.status_id,
      },
      optionStatus: [],
      optionProject: [],
    };
  },
  validations: {
    form: {
      name: {
        required
      },
      time: {
        required
      },
      project_id: {
        required
      },
      status_id: {
        required
      },
    }
  },
  watch: {
    items: {
      handler: function (val) {
        if (val) {
          this.form.name = val.name
          this.form.time = val.time
          this.form.project_id = val.project_id
          this.form.status_id = val.status_id
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
      this.form.time = null
      this.form.project_id = null
      this.form.status_id = null
      this.$v.$reset();
    },
    async getStatus() {
      this.$store.dispatch("status/getStatus", {  })
        .then((resp) => {
          this.optionStatus = resp
        })
        .catch((error) => {
        });
    },
    async getProject() {
      this.$store.dispatch("project/index", {  })
        .then((resp) => {
          this.optionProject = resp
        })
        .catch((error) => {
        });
    },
  },
  async created() {
    await this.getStatus()
    await this.getProject()
  },
  mounted() {
  }
};
</script>
