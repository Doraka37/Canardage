const initialState = {
  pseudo: "",
  userList: []
};

function UserInfos(state = initialState, action) {
  let nextState;
  switch (action.type) {
    case 'SET_PSEUDO':
      nextState = {
        ...state,
        pseudo: action.value
      };
      return nextState;
    case 'SET_USER_LIST':
      nextState = {
        ...state,
        userList: action.value
      };
      return nextState;
    default:
      return state;
  }
}

export default UserInfos;
