const initialState = {
  pseudo: ""
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
    default:
      return state;
  }
}

export default UserInfos;
