# Upper-taper clamping between two raw right edges

Research theorem, 5 November 2026. Both physical
raw edges and their independent optimizing rows remain present.

Let an unselected center have type \(\alpha\in\{0,1\}\),
\[
 t\in[.45,.5],\quad z=t+ikR(t),\quad R(t)=400(.5-t)^2,
 \quad q=1+ikR'(t),\quad
 k\in\begin{cases}[-.03,.02],&\alpha=0,\\ {}[-.057,0],&\alpha=1.\end{cases}
 \tag{1}
\]
Both neighboring right targets have been fixed at \(.5\) by the
complete raw source reduction. The incoming edge has own-factorial
indicator \(\alpha\); the outgoing edge has its right neighbor's
indicator \(\beta\in\{0,1\}\). The type of the incoming right
neighbor contributes only a constant to the center marginal.

Use the original real-row stationarity equation and allocated raw
marginal of [the mixed clamping theorem](research_mixed_raw_coherent_right_clamping.md),
equations (2)--(3). Write \(u_0,u_1\) for the independent maximizing
rows, with orientations zero and one and own indicators \(\alpha,\beta\).
The required complete family consists of just four pairs
\((\alpha,\beta)\). **Theorem 1.** Throughout (1),
\[
 D=\Re\{q[K_0(z,u_0)+K_1(z,u_1)]\}<-1/20.\tag{2}
\]
No complex critical-point equation is imposed on either raw row.

For each real parameter differential, the checker evaluates
\[
 \begin{split}
 dz&=q\,dt+iR\,dk,&dq&=i(800k\,dt+R'\,dk),\\
 du_d&=-\Re((K_d)_u dz)/(T_d)_u,&(T_d)_u&\le-2\pi,\\
 dD&=\Re\left\{dq(K_0+K_1)
       +q\sum_{d=0}^1[(K_d)_z dz+(K_d)_u du_d]\right\}.
 \end{split}\tag{3}
\]
Each row is enclosed by a validated midpoint trial and the whole-cell
mean-value estimate using \((T_d)_u\le-2\pi\). The checker bounds
(2) both directly and by midpoint plus full-box derivative radii.
Its exact binary partitions cover both real parameters in (1);
strict monotonicity may retain only the maximizing face. A saved
replay rechecks every leaf and every such reduction. There are no
complex root solves, and no equality between the two rows is assumed.

The complete outward certificate accepts all four domains, with
29 cells. Integrating (2) at fixed \(k\) gives an upper-rate loss
\((t-.45)/20\) on clamping to \(.45\). Every left cutoff is one
throughout the motion, so the actual hybrid neighboring heights stay
fixed. The moving type-four center is unselected and has nonpositive
height; its full Fourier upper envelope has the factorial branch up
to the half endpoint by continuity. Selections at the two real right
neighbors contribute constant factors to the comparison. All finite
rows and the original single source tolerance remain in the upper
bound; no relative lower bound for a raw kernel is asserted.

A two-cycle retains its two opposite physical edges and their two
independent rows. A one-cycle cannot have a distinct upper-taper
center and a right neighbor, so is outside this local configuration.
This result does not clamp a selected center directly or establish
a full-period estimate.

    python3 experiments/certify_mixed_two_raw_right_clamping.py
