<template>
  <div>
    <div class="row">
      <div class="col-xl-12">
        <div class="card">
          <div class="card-header">
            <h3>List Project</h3>
          </div>
          <div class="card-body">
            <div class="row mb-2">
              <div class="col-xl-6">
                <a class="btn btn-success btn-icon-split" v-on:click="newProject()">
                  <span class="icon text-white-50">
                    <i class="fas fa-plus"></i>
                  </span>
                  <span class="text">Make a new project</span>
                </a>
              </div>
            </div>
            <div class="row">
              <div class="col-xl-12">
                <table class="table table-bordered borderBlack mb-2">
                  <thead>
                    <!-- <tr class="bg-primary">
                <th colspan="5" class="text-white">DIKDIK MUSFAR</th>
              </tr> -->
                    <tr class="softGreen">
                      <th width="5%" scope="col">No</th>
                      <th width="10%" scope="col">Project Name</th>
                      <th width="25%" scope="col">Description</th>
                      <th width="15%" scope="col">Start Date</th>
                      <th width="15%" scope="col">Estimated Time</th>
                      <th width="15%" scope="col">Created</th>
                      <th width="15%" scope="col">Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, idx) in table.items" :key="idx" v-if="(table.items).length > 0">
                      <th scope="row">{{ idx + 1 }}</th>
                      <td>{{ item.name }}</td>
                      <td>{{ item.description }}</td>
                      <td>{{ item.start_date }}</td>
                      <td>{{ item.estimated_time }} days</td>
                      <td>{{ item.created_at }}</td>
                      <td>
                        <b-button v-on:click="show(item.id, item.name)" size="sm" variant="info">
                          <i class="fas fa-eye"></i>
                        </b-button>
                        <b-button v-on:click="deleteProject(item.id, item.name)" size="sm" variant="danger">
                          <i class="fas fa-trash"></i>
                        </b-button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <b-modal id="modal-create-form" centered size="lg" title="Make a new project" title-class="font-27" hide-footer
        no-close-on-backdrop>
        <div class="row">
          <div class="col-12">
            <project-form ref="revisi" :items="form" @input="submitCreate"></project-form>
          </div>
        </div>
      </b-modal>
      <b-modal id="modal-show" centered size="lg" title="Show task from a project" title-class="font-27" hide-footer
        no-close-on-backdrop>
        <div class="row">
              <div class="col-xl-12">
                <table class="table table-bordered borderBlack mb-2">
                  <thead>
                    <!-- <tr class="bg-primary">
                <th colspan="5" class="text-white">DIKDIK MUSFAR</th>
              </tr> -->
                    <tr class="softGreen">
                      <th width="5%" scope="col">No</th>
                      <th width="10%" scope="col">Project Name</th>
                      <th width="25%" scope="col">Project Task</th>
                      <th width="15%" scope="col">Estimated Time</th>
                      <th width="15%" scope="col">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, idx) in tasks" :key="idx" v-if="tasks.length > 0">
                      <th scope="row">{{ idx + 1 }}</th>
                      <td>{{ item.project.name }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.time }}</td>
                      <td>{{ item.status.name }} days</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import projectForm from '~/components/Project/form'


export default {
  name: 'Project',
  layout: 'base',
  components: {
    projectForm
  },
  data() {
    return {
      number: 0,
      table: {
        items: [],
      },
      form: {
        id: null,
        name: null,
        description: null,
        start_date: null,
      },
      tasks: [],
    }
  },
  methods: {
    async getListProject() {
      this.$store.dispatch("project/index", {})
        .then((resp) => {
          this.table.items = resp
        })
        .catch((error) => {
        });
    },
    submitCreate(projectForm) {
      let form = projectForm;
      this.$store
        .dispatch("project/store", { form })
        .then((resp) => {
          this.getListProject();
          this.$bvModal.hide('modal-create-form')
          this.form.name = null;
          this.form.start_date = null;
          this.form.description = null;
          Swal.fire("Success!", "New project has been created", "success");
        })
        .catch((error) => {
        });
    },
    deleteProject(id, name) {
      Swal.fire({
        title: "Delete project?",
        text: "Are you sure you want to delete" + name + "?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#16A75C",
        cancelButtonColor: "#E53935",
        confirmButtonText: "Yes",
        cancelButtonText: "Cancel"
      }).then(result => {
        if (result.value) {
          this.$store.dispatch("project/deleteProject", { id: id })
            .then((resp) => {
              Swal.fire("Success!", "Project has been deleted!", "success")
                .then((result) => {
                  this.getListProject();
                });
            })
            .catch((error) => {
              Swal.fire("Error!", "Failed to delete project", "danger");
            });
        }
      });
    },
    newProject() {
      this.$bvModal.show('modal-create-form')
    },
    show(id) {
      this.$store.dispatch("project/showProject", { id: id })
        .then((resp) => {
          this.tasks = resp
          this.$bvModal.show('modal-show')
        })
        .catch((error) => {
        });
    },
  },
  async created() {
    await this.getListProject();
  },
}
</script>
