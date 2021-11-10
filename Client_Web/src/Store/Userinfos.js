const initialState = {
  pseudo: "",
  userList: [],
  hand: [6, 7, 13],
  playerID: 0,
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
    case 'SET_HAND':
      nextState = {
        ...state,
        hand: action.value
      };
      return nextState;
    case 'SET_PLAYER_ID':
      nextState = {
        ...state,
        playerID: action.value
      };
      return nextState;
    default:
      return state;
  }
}

export default UserInfos;
