import * as axios from "axios";



const instance = axios.create(
    {
        withCredentials: true,
        baseURL: 'https://social-network.samuraijs.com/api/1.0/',
        headers: {
            "API-KEY": "a0d25507-a821-41ad-8d3e-c4269e207d98"
        }
    });

export  const usersApi= {
    getUsers(currentPage = 1, pageSize = 10) {
        return instance.get(`users?page=${currentPage}&count=${pageSize}`)
            .then(response => {
                return response.data
            });
    },
    follow(userId) {
       return  instance.post(`follow/${userId}`)
    },
    unfollow(userId) {
        return  instance.delete(`follow/${userId}`)
            },
    getProfile(userId) {
        return  instance.get(`profile/` + userId);

    }
}

 export const authApi={
    me(){
      return   instance.get(`auth/me`)
    }

 }
