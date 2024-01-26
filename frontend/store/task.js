export const state = () => ({});

export const mutations = {};

export const getters = {};

export const actions = {

  index({ commit, dispatch, getters }, {  } = {}) {
    return this.$axios
      .$get("/tasks/", { })
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  getTask({ commit, dispatch, getters }, { id } = {}) {
    return this.$axios
      .$get("/tasks/" + id + "/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  store({ commit, dispatch, getters }, { form } = {}) {
    return this.$axios
      .$post("/tasks/", form)
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  update({ commit, dispatch, getters }, { id, form } = {}) {
    return this.$axios
      .$put("/tasks/" + id +"/update/", form)
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },

  deleteProject({ commit, dispatch, getters }, { id } = {}) {
    return this.$axios
      .$delete("/tasks/" + id +"/delete/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },
};
