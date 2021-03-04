import { useAuth } from "../Auth";
import React from 'react';

function ProfileHome () {
  const { setToken } = useAuth();

  function logOut() {
    setToken(false);
  }

  return (
    <div>
      <div>Admin Page</div>
      <button class="w-100 btn btn-lg btn-primary" onClick={logOut}>Log out</button>
    </div>
  );
}

export default ProfileHome;