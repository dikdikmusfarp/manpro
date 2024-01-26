export const state = () => ({});

export const mutations = {};

export const getters = {};

export const actions = {
  getStatus({ commit, dispatch, getters }, {  } = {}) {
    return this.$axios
      .$get("/statuses/")
      .then((res) => {
        return Promise.resolve(res);
      })
      .catch(function (error) {
        return Promise.reject(error);
      });
  },
};
