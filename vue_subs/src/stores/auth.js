import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
  }),
  actions: {
    async login(credentials) {
      try {
        const response = await axios.post('/api/v1/auth/jwt/create/', credentials);

        this.accessToken = response.data.access;
        this.refreshToken = response.data.refresh;

        console.log(this.accessToken);

        // Fetch user details
        const userResponse = await axios.get('/api/v1/auth/users/me/', {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        });

        this.user = userResponse.data;

        console.log(this.user);

        // Save tokens in localStorage for persistence
        localStorage.setItem('accessToken', this.accessToken);
        localStorage.setItem('refreshToken', this.refreshToken);
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    logout() {
      this.user = null;
      this.accessToken = null;
      this.refreshToken = null;
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
    loadTokensFromStorage() {
      this.accessToken = localStorage.getItem('accessToken');
      this.refreshToken = localStorage.getItem('refreshToken');

      if (this.accessToken) {
        axios
          .get('/auth/users/me/', {
            headers: { Authorization: `Bearer ${this.accessToken}` },
          })
          .then((response) => {
            this.user = response.data;
          })
          .catch((error) => {
            console.error('Error loading user from token:', error);
            this.logout();
          });
      }
    },
  },
});
