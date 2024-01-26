export const state = () => ({});

export const mutations = {};

export const getters = {};

export const actions = {

  index({ commit, dispatch, getters }, {  } = {}) {
    return this.$axios
      .$get("/projects/", { })
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  getProject({ commit, dispatch, getters }, { id } = {}) {
    return this.$axios
      .$get("/projects/" + id + "/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  store({ commit, dispatch, getters }, { form } = {}) {
    return this.$axios
      .$post("/projects/", form)
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  update({ commit, dispatch, getters }, { id, form } = {}) {
    return this.$axios
      .$put("/projects/" + id +"/update/", form)
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  deleteProject({ commit, dispatch, getters }, { id } = {}) {
    return this.$axios
      .$delete("/projects/" + id + "/delete/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  showProject({ commit, dispatch, getters }, { id } = {}) {
    return this.$axios
      .$get("/projects/" + id + "/tasks/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },
};
