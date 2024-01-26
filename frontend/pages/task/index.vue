<template>
  <div>
    <div class="row">
      <div class="col-xl-12">
        <div class="card">
          <div class="card-header">
            <h3>List Task</h3>
          </div>
          <div class="card-body">
            <div class="row mb-2">
              <div class="col-xl-6">
                <a class="btn btn-success btn-icon-split" v-on:click="newProject()">
                  <span class="icon text-white-50">
                    <i class="fas fa-plus"></i>
                  </span>
                  <span class="text">Make a new Task</span>
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
                      <th width="10%" scope="col">Task Name</th>
                      <th width="25%" scope="col">Status</th>
                      <th width="15%" scope="col">Estimated Time</th>
                      <th width="15%" scope="col">Project</th>
                      <th width="15%" scope="col">Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, idx) in table.items" :key="idx" v-if="(table.items).length > 0">
                      <th scope="row">{{ idx + 1 }}</th>
                      <td>{{ item.name }}</td>
                      <td>{{ item.status_id }}</td>
                      <td>{{ item.time }} days</td>
                      <td>{{ item.project_id }}</td>
                      <td>
                        <b-button v-on:click="editTask(item.id)" size="sm" variant="warning">
                          <i class="fas fa-pen"></i>
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
      <b-modal id="modal-create-form" centered size="lg" title="Make a new task" title-class="font-27" hide-footer
        no-close-on-backdrop>
        <div class="row">
          <div class="col-12">
            <task-form ref="revisi" :items="form" @input="submitCreate"></task-form>
          </div>
        </div>
      </b-modal>
      <b-modal id="modal-update-form" centered size="lg" title="Update a task" title-class="font-27" hide-footer
        no-close-on-backdrop>
        <div class="row">
          <div class="col-12">
            <task-form ref="revisi" :items="form" @input="submitUpdate"></task-form>
          </div>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import taskForm from '~/components/Task/form'


export default {
  name: 'Project',
  layout: 'base',
  components: {
    taskForm
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
        project_id: null,
        time: null,
        status_id: null,
      }
    }
  },
  methods: {
    async getListProject() {
      this.$store.dispatch("task/index", {})
        .then((resp) => {
          this.table.items = resp
        })
        .catch((error) => {
        });
    },
    submitCreate(taskForm) {
      let form = taskForm;
      this.$store
        .dispatch("task/store", { form })
        .then((resp) => {
          this.getListProject();
          this.$bvModal.hide('modal-create-form')
          this.form.name = null;
          this.form.project_id = null;
          this.form.time = null;
          Swal.fire("Success!", "New project has been created", "success");
        })
        .catch((error) => {
        });
    },
    deleteProject(id, name) {
      Swal.fire({
        title: "Delete task?",
        text: "Are you sure you want to delete" + name + "?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#16A75C",
        cancelButtonColor: "#E53935",
        confirmButtonText: "Yes",
        cancelButtonText: "Cancel"
      }).then(result => {
        if (result.value) {
          this.$store.dispatch("task/deleteProject", { id: id })
            .then((resp) => {
              Swal.fire("Success!", "Task has been deleted!", "success")
                .then((result) => {
                  this.getListProject();
                });
            })
            .catch((error) => {
              Swal.fire("Error!", "Failed to delete task", "danger");
            });
        }
      });
    },
    newProject() {
      this.$bvModal.show('modal-create-form')
    },
    editTask(id) {
      this.form.id = id
      this.getTask()
      this.$bvModal.show('modal-update-form')
    },
    getTask() {
      this.$store.dispatch("task/getTask", { id: this.form.id })
        .then((resp) => {
          this.form.name = resp.name
          this.form.time = resp.time
          this.form.status_id = resp.status_id
          this.form.project_id = resp.project_id
          // this.tasks = resp
        })
        .catch((error) => {
        });
    },
    submitUpdate(taskForm) {
      let form = taskForm;
      this.$store
        .dispatch("task/update", { id: this.form.id, form })
        .then((resp) => {
          this.getListProject();
          this.form.id = null;
          this.form.name = null;
          this.form.time = null
          this.form.status_id = null
          this.form.project_id = null
          this.$bvModal.hide('modal-update-form')
          Swal.fire("Success!", "Product has been updated", "success");
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
