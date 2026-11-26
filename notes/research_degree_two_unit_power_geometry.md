# The marked boundary action at a degree-two power \(1\) or \(-1\)

The isolated degree-two geometry exists at both unit powers.
Its boundary potential can be compared directly with the
bare edge, without inferring geometry from a quantum identity.

Let \(\sigma\in\{1,-1\}\). Use the original edge phase
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                 \bigl(\tan(t/2)\cos(u/2)\bigr),
\]
with its complete normalization. The filled geometric action is
\[
 G_\sigma(u,v)=\operatorname{stat}_t
 \left[\psi(t,u)+\psi(t,v)+\frac{i\sigma}{4\pi}t^2-it\right].
 \tag{1}
\]
The selected branch and all its positive edge shapes are proved in
[the isolated-vertex geometry note](research_isolated_internal_vertex_geometry.md).
At \(u=v=0\) it satisfies
\(\cos(t/2)=1+i\sigma\), with
\(\sigma\Re t>0\) and \(\Im t<0\).

**Proposition.** On a neighborhood of the original complete
outside boundary,
\[
 dG_\sigma
   =d\left[\psi(u,v)-\frac{i\sigma}{4\pi}(u^2+v^2)\right],
 \tag{2}
\]
and
\[
 \Re G_\sigma(0,0)=\psi(0,0).
 \tag{3}
\]
Consequently the source phase on the right of (2) has exactly
the original primitive boundary-period derivatives and the
absolute real volume normalization. The original filled core
and its primitive slope remain part of this geometric piece.

**Proof.** Put
\[
 \alpha=u/2,\quad\beta=v/2,\quad
 D=\sqrt{1-\sin^2\alpha\sin^2\beta},\quad
 k=\cos\alpha\cos\beta+i\sigma D,
 \tag{4}
\]
where \(D(0,0)=1\). Define \(t\) by \(\cos(t/2)=k\), using
the selected branch at zero. It is holomorphic because the
selected sine is nonzero. The elementary identity
\[
 k^2-2\cos\alpha\cos\beta\,k+\cos^2\alpha+\cos^2\beta=0
 \tag{5}
\]
verifies its stationary equation as follows. Write
\(\zeta=t/2\), \(h=\sin\zeta\), and
\[
 Q_\alpha=-i\sigma(\cos\alpha\,k-\cos\beta),\qquad
 Q_\beta=-i\sigma(\cos\beta\,k-\cos\alpha).
\]
Equation (5) gives
\[
 Q_\alpha^2=\cos^2\alpha+k^2\sin^2\alpha,\qquad
 Q_\beta^2=\cos^2\beta+k^2\sin^2\beta.
\]
At zero both \(Q\)'s equal \(1\), so these are the square-root
branches in the two selected inverse hyperbolic sines.
With \(w=k+i\sigma h=e^{i\sigma\zeta}\),
\[
 \frac{(h\cos\alpha+Q_\alpha)
       (h\cos\beta+Q_\beta)}{k^2}
 =-\frac{\cos\alpha\cos\beta(1+w^2)
           -(\cos^2\alpha+\cos^2\beta)w}{k^2}
 =-w.
\]
Thus the exponential of the stationary equation holds.
Its logarithm is the original one at \(u=v=0\), by the selected
unit-power solution. Holomorphic continuation retains that
logarithm nearby. The isolated geometric uniqueness theorem
therefore identifies (4) with the original critical branch.

Now set \(A=\operatorname{arsinh}(\tan\alpha\cos\beta)\).
Since \(\cosh A=D/\cos\alpha\),
\[
 \sinh(A+i\sigma\alpha)
      =\tan\alpha\,(\cos\alpha\cos\beta+i\sigma D)
      =\tan\alpha\,k.
\]
All terms vanish at \(\alpha=0\), so the selected germs satisfy
\[
 \operatorname{arsinh}(\tan\alpha\,k)
       =\operatorname{arsinh}(\tan\alpha\cos\beta)
                                     +i\sigma\alpha. \tag{6}
\]
The envelope rule in (1), symmetry of \(\psi\), and (6) give
\[
 (G_\sigma)_u=\psi_u(u,v)-\frac{i\sigma}{2\pi}u.
\]
The analogous formula in \(v\) proves (2).
The exact geometric degree–power symmetry and the terminal
two-crossing volume, as proved in
[the isolated action-gap note](research_isolated_vertex_action_gap.md),
give \(M_{2,\pm1}=M_\infty=\psi(0,0)\). This proves (3).
The possible additive constant in (2) is therefore purely
imaginary. Its value is not needed for the real volume or the
peripheral derivatives; exact quantum unit factors are retained
by the separate source theorem. \(\square\)

This comparison permits the original \(P_{2,\pm1}\) pieces to
be used in a finite collection of two-boundary geometric kernels.
Their positive geometric charts and core orientations come
from the original isolated filling, and their two boundary
labels are unchanged. They are not being replaced by an
unmarked edge when attached to another piece.

If one instead draws the reduced tangle, the
[marked unit-power move](research_marked_degree_two_tangle_moves.md)
must be used with its actual half-turn:
\[
 T(R^\sigma T(F))
       \simeq R^{-\sigma}T(R^{-\sigma}K(F)).
\]
Both adjacent crossing shifts and the proper rotation of the
entire marked spectator \(F\) are retained. The quadratic
terms in (2) are precisely the corresponding boundary action
terms. They are not an instruction to add half an integral
longitude to a meridian on a fixed marked torus.

