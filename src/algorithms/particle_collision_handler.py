from ..constants.simulation import COR

def collision_handler(particles: list) -> list:
    # Loop over each pair of particles (excluding repeats)
    for i in range(0, len(particles)-1):
        for j in range(i+1, len(particles)):
            # Check if the particles have different IDs
            if particles[i].ID == particles[j].ID:
                continue  # Skip this pair if they have the same ID

            # Calculate the vector between the positions of the particles
            dydx = particles[j].pos - particles[i].pos
            # Calculate the distance between the particles
            distance = dydx.magnitude()
            
            # Check if the particles are colliding
            if distance <= 2 * particles[i].radius:
                # Calculate the normalised vector along the line of centers
                nynx = dydx / distance

                # Calculate the relative velocity of the particles along the normal vector
                dvydvx = particles[j].vel - particles[i].vel
                relative_vel = dvydvx.dot(nynx)

                # Calculate the impulse (change in momentum) due to the collision
                impulse = 2 * relative_vel * COR  # COR: Coefficient of restitution

                # Calculate the change in velocity for each particle
                dv1 = (impulse * nynx) / particles[i].mass
                dv2 = -1 * (impulse * nynx) / particles[j].mass

                # Update the velocities of the particles
                particles[i].vel += dv1
                particles[j].vel += dv2

                # Calculate the overlap between the particles
                overlap = (2 * particles[i].radius) - distance
                # Calculate the separation distance to resolve the overlap
                separation = 0.5 * overlap * nynx

                # Move the particles to resolve the overlap
                particles[i].pos -= separation  # Move particle i
                particles[j].pos += separation  # Move particle j in the opposite direction

    return particles