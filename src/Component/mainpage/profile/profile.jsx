import React, { useState, useEffect } from 'react';
import auth from 'firebase';

const Profile = ({ user }) => {
  const [userData, setUserData] = useState(user);
  const [editing, setEditing] = useState(false);

  const handleEditClick = () => {
    setEditing(true);
  };

  const handleSaveClick = async () => {
    try {
      // Make an API call to update user data
      await axios.put('/api/user', userData);
      setEditing(false);
    } catch (error) {
      console.error('Error updating user data:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData((prevData) => ({ ...prevData, [name]: value }));
  };

  useEffect(() => {
    // Fetch user data when the component mounts
    const fetchUserData = async () => {
      try {
        const response = await axios.get('/api/user');
        setUserData(response.data);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, []);

  return (
    <div>
      <h1>Profile</h1>
      {editing ? (
        <>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={userData.name}
            onChange={handleInputChange}
          />
          {/* Add other input fields for profile editing */}
          <button onClick={handleSaveClick}>Save</button>
        </>
      ) : (
        <>
          <p>Name: {userData.name}</p>
          {/* Display other user information */}
          <button onClick={handleEditClick}>Edit Profile</button>
        </>
      )}
    </div>
  );
};

export default Profile;
