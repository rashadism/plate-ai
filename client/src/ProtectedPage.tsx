import Navbar from './Navbar';

function ProtectedPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-50 to-green-50">
      <Navbar />
      <div className="p-8 text-center text-gray-600 text-lg">Protected content goes here.</div>
    </div>
  );
}

export default ProtectedPage; 