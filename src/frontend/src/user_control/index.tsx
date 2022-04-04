export interface UserInterface {
    isLoggedIn: boolean,
    email: string | null,
    userId: number | null,  // maybe gets removed
    username: string | null
}


const User: UserInterface = {
    isLoggedIn: false,
    email: null,
    userId: null,
    username: null
}

export default User
