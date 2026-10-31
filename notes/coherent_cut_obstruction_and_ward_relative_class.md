# Coherent cuts retain a zero mode; an exact relative E-Ward class

This note proves that a Gaussian rank-one cut probe cannot remove both
framing zero modes at an unchanged geometric critical point. It then
constructs an exact finite Ward current and relative class using the
actual nilpotent \(E\)-action. The latter is genuine quantum boundary
transport, but has not been identified with the internal geometric
centralizer flow or its sourced Gaussian pushforward.

## 1. Conservation leaves one cut position, even for a rank-one probe

Every actual positive or negative crossing has position update

\[
 (a,b)\longmapsto(b+k,a-k),\qquad
 (a,b)\longmapsto(b-k,a+k),
\]

respectively. Both conserve the total integer position. Close all strands
except one by the actual pivotal trace. Along every surviving state,
the other output positions equal their input positions. Conservation
then forces

\[
 a_{\mathrm{out}}=a_{\mathrm{in}}.                                      \tag{1.1}
\]

This is an exact support equation, before taking a critical point or a
root specialization. The auxiliary off-root cut matrix is diagonal too.
Diagonal factorial changes of frame do not alter this fact.

Thus the rank-one probe
\[
 \frac{\phi C_N\psi}{\phi\psi}
\]
has only one cut index in its actual state sum. Taking
\[
 \psi_a=z^a q^{ca^2},\qquad \phi_a=w^a q^{da^2}
\]
gives exactly

\[
 \frac{\sum_{a=0}^{N-1}(zw)^a q^{(c+d)a^2}(C_N)_{aa}}
      {G_N},\qquad
 G_N=\sum_{a=0}^{N-1}(zw)^a q^{(c+d)a^2}.                       \tag{1.2}
\]

The denominator is retained and must be nonzero. At the actual root,
scalarity of the cut operator makes (1.2) exactly \(F_N\).
There are still \(m+1\) independent flow variables for an \(m\)-crossing
knot braid, rather than \(m+2\). Introducing two symbols for the cut
endpoints does not make them independent.

## 2. Exact rank-one obstruction at the geometric critical point

Let \(H=\operatorname{Log} Q\), \(q=\exp(H/2)\), \(q_1=H a\), and
\(\kappa_c=c+d\). The added leading boundary phase in (1.2) is

\[
 g(q_1)=\operatorname{Log}(zw)\,q_1+\frac{\kappa_c}{2}q_1^2.                  \tag{2.1}
\]

Its normalization \(G_N\) is independent of all internal variables.
Even when \(z,w\) depend on the external meridian, it has no internal
Hessian contribution.

The original geometric critical phase has a two-dimensional radical,
the actual framed \(B_1\)-torsor. On its regular chart,

\[
 A_{\mathrm{cut}}=\frac{M}{M+s},\qquad q_1=\log A_{\mathrm{cut}},
\qquad
 dq_1=-\frac{ds}{M+s}.                                        \tag{2.2}
\]

In particular it is independent of the residual centralizer coordinate
\(r\), whose fundamental vector is
\[
 V_J=\Delta\partial_r,\qquad
 \Delta=s+(M-M^{-1})r.
\]

For the same geometric point to remain critical after (2.1), one must
have \(g'(q_1^*)=0\) on the chosen logarithmic sheet. Indeed \(dq_1\ne0\)
there. At that point the full Hessian changes by

\[
 H_{\mathrm{new}}=H_{\mathrm{old}}+\kappa_c\,dq_1\otimes dq_1.             \tag{2.3}
\]

On the two-dimensional original radical, its matrix in the framing
coordinates is therefore

\[
 \begin{pmatrix}0&0\\0&\kappa_c/(M+s)^2\end{pmatrix}.             \tag{2.4}
\]

Consequently \(\partial_r\) remains in the full Hessian kernel. If
\(\kappa_c\ne0\), the old Hessian has exactly that two-dimensional kernel,
and \(dq_1\) is nonzero on it, the new corank is exactly one. To check
the last assertion, project \(H_{\mathrm{new}}v=0\) to the old cokernel;
it forces \(dq_1(v)=0\), then \(H_{\mathrm{old}}v=0\).

Thus a coherent Gaussian cut can generically remove one framing mode,
but cannot remove both at an unchanged geometric critical point.
The exact Gauss-sum normalization does not change this obstruction.
This result does not assume that a differently moved coherent critical
scheme has already been identified with a holonomy scheme.

## 3. An explicit finite E-Ward current

Use the actual factorial boundary frame of
[the marked cut calculation](marked_braid_holonomy.md). Write
\[
 \mathcal E=\rho^2E,\qquad \rho=q-q^{-1},\qquad x=-M/q.
\]
It is upper bidiagonal:

\[
 \mathcal E_{a,a+1}=\epsilon_a
   =q^{-1}x^{-1}(1-x^2Q^{-a})
   =M Q^{-a-1}-M^{-1},\qquad 0\le a<N-1,                     \tag{3.1}
\]

and its last wrap is zero. At \(M=1\),
\[
 \epsilon_a=Q^{-a-1}-1,
\]
which is nonzero for every interior edge \(0\le a<N-1\).
Hence these coefficients are units in the whole meridian germ near
completion. The exact actual intertwining identity gives
\[
 [\mathcal E,C_N]=0.
\]
Since \(C_N\) is diagonal by (1.1), this reads

\[
 \epsilon_a\big((C_N)_{a+1,a+1}-(C_N)_{aa}\big)=0.             \tag{3.2}
\]

It independently connects all its diagonal entries.

Let \(w,w'\) be any two diagonal probe weights with
\(\sum_a w_a=\sum_a w'_a=1\), and put
\[
 r_a=w_a-w'_a,\qquad j_a=\sum_{b=0}^a r_b
 \quad(0\le a<N-1).
\]
Define the strictly lower-bidiagonal current
\[
 B_{a+1,a}=\frac{j_a}{\epsilon_a}.                              \tag{3.3}
\]
Direct matrix multiplication gives the exact identity

\[
 \boxed{[\mathcal E,B]=\operatorname{diag}(r_0,\ldots,r_{N-1}).} \tag{3.4}
\]

Indeed its diagonal is \(j_a-j_{a-1}\), with \(j_{-1}=j_{N-1}=0\);
both products have no other entries. It follows that

\[
 \sum_a(w_a-w'_a)(C_N)_{aa}
 =\operatorname{Tr}([\mathcal E,B]C_N)
 =\operatorname{Tr}(B[C_N,\mathcal E])=0.                       \tag{3.5}
\]

This is an exact source transgression for the finite cut, including
its endpoints. For the average \(w_a=1/N\) and the endpoint probe
\(w'_a=\delta_{a0}\), it is explicitly
\[
 j_a=(a+1)/N-1.
\]

Equivalently, the actual weighted interval difference
\[
 (Df)_a=\epsilon_a(f_{a+1}-f_a)
\]
gives an exact complex
\[
 0\longrightarrow k\longrightarrow k^N
       \xrightarrow{D}k^{N-1}\longrightarrow0.                 \tag{3.6}
\]
Surjectivity is solved by the cumulative sum
\(f_0=0,\ f_a=\sum_{b<a}(Df)_b/\epsilon_b\).
Its dual says that normalized probes differ by a unique edge current.
No endpoint term is discarded.

The cyclic coefficient that was removed in (3.1) is also exact:
\[
 \epsilon_{N-1}^{\mathrm{cyc}}
   =q^{-1}x^{-1}(1-M^2)=M-M^{-1}.                             \tag{3.7}
\]
It is the original whole-meridian nilpotent endpoint defect, rather
than an arbitrary choice of cyclic representative. Its vanishing
at \(M=1\) does not permit deleting its meridian normal derivative.
In particular its scalar is exactly the regular-meridian eigenvalue
gap; this coincidence alone does not identify the two group actions.

## 4. A literal finite additive flow from the actual E

The matrix \(\mathcal E\) is nilpotent of order \(N\). Therefore

\[
 G_t=\exp(t\mathcal E)
     =\sum_{j=0}^{N-1}\frac{t^j\mathcal E^j}{j!}                 \tag{4.1}
\]

is an exact polynomial action of the additive group:
\(G_{t+u}=G_tG_u\), \(G_t^{-1}=G_{-t}\).
It commutes with \(C_N\). This uses the actual \(E\)-matrix,
not an auxiliary action on an unrelated coefficient space.

There is an explicit translation presentation. On the basis \(w_j\),
set
\[
 I(w_j)=\frac{\epsilon_0\cdots\epsilon_{j-1}}{j!}\,\xi^j
       \quad(0\le j<N).
\]
All coefficients are units near \(M=1\), and
\[
 I\mathcal E=\partial_\xi I,\qquad
 I G_t I^{-1}f(\xi)=f(\xi+t).                                 \tag{4.2}
\]

This flow is natural for actual \(E\)-intertwiners. If
\(A\mathcal E_V=\mathcal E_W A\), finite powers give
\(A G_t^V=G_t^W A\). The same applies to the actual coproduct
on tensor products and the actual crossing/turn maps. At a primitive
root, the \(Q\)-binomial identity for
\(\Delta E=E\otimes K+1\otimes E\) gives
\((\Delta E)^N=0\), so the tensor-product exponential also truncates.

No proper \(q\)-hypergeometric form or asymptotic bound is asserted
for the ordinary factorial change in (4.2).

## 5. The exact relative Ward class

Let \(W=\operatorname{End}_k(V_N)\) and
\(\mathscr D=\operatorname{ad}\mathcal E\).
It is nilpotent of order at most \(2N-1\). On \(W[t]\), use the twisted
relative complex

\[
 \delta_{\mathcal E}h
   =(\partial_t h-\mathscr D h,\ h(0),\ h(1)),
\qquad
 W[t]\longrightarrow W[t]\oplus W\oplus W.                    \tag{5.1}
\]

Its transgression is the finite polynomial expression

\[
 \boxed{L_{\mathcal E}(a,b_0,b_1)
   =\int_0^1 e^{-t\mathscr D}a(t)\,dt
       -e^{-\mathscr D}b_1+b_0.}                              \tag{5.2}
\]

The identity
\[
 \partial_t(e^{-t\mathscr D}h)
   =e^{-t\mathscr D}(\partial_t h-\mathscr D h)
\]
proves \(L_{\mathcal E}\delta_{\mathcal E}=0\).
The gauge \(h\mapsto e^{-t\mathscr D}h\), with the same endpoint gauges,
identifies (5.1) with the ordinary relative polynomial complex.
Thus its first cohomology is zero and its second cohomology is \(W\).

For the actual normalized rank-one projector \(P=\psi\phi\),
\(\phi\psi=1\), set \(P_t=G_tPG_t^{-1}\).
There is an exact section and marked class

\[
 i_{\mathcal E}(P)=(P_t,0,0),\qquad
 L_{\mathcal E}i_{\mathcal E}(P)=P.                            \tag{5.3}
\]

Pairing with the actual cut gives

\[
 \boxed{\operatorname{Tr}\big(C_N
       L_{\mathcal E}i_{\mathcal E}(P)\big)=F_N.}                \tag{5.4}
\]

The normalization is unchanged. Moreover
\[
 \delta_{\mathcal E}(tP_t)=(P_t,0,P_1),
\]
so the endpoint co-source is visible: the relative class
\((P_t,0,0)\) is not killed by its ordinary twisted primitive.
This is an exact Ward-flow relative boundary theorem.

## 6. What has not been identified

The geometric centralizer \(J_M\) is multiplicative away from \(M=1\)
and additive at \(M=1\); the finite flow (4.1) remains additive for
all \(M\). They cannot be equated as whole meridian group schemes.
In addition, unscaled \(e^{t\mathcal E}\) is an amplitude-scale flow
in a semiclassical expansion. A finite canonical flow requires a
generator divided by \(H=\operatorname{Log} Q\).

There is a useful exact candidate at the special fiber:
\(-\log(1+\mathcal E)\) is a finite nilpotent polynomial.
Its principal cut symbol at \(M=1,\ p_{\mathrm{cut}}=1\) is
\[
 -\log(1+e_{\mathrm{cut}})=-\log(1+s)=\log A_{\mathrm{cut}}.
\]
The already established geometric form obeys
\[
 \iota_{V_J}\Omega_{\mathrm{cut}}=d\log A_{\mathrm{cut}}.
\]
This matches a scalar Hamiltonian on the framed chart. It does not
prove that the full internal Ward action becomes \(V_J\), because
the reduced density form and the bulk internal shift complex still
need their marked chain comparison.

Thus (5.4) supplies actual finite source transport and endpoints.
It does not yet supply the weighted internal-shift covariance or
external-meridian compatibility required in section 4 of
[the sourced telescoping criterion](sourced_telescoping_geometric_support_criterion.md).
Neither geometric support nor a selected volume asymptotic follows
from the coherent probe or this boundary relative class alone.

The [cyclic Ward norm adapter](cyclic_ward_norm_adapter.md) completes
the literal missing edge kappa and proves an exact determinant
character at the Frobenius peripheral value M^N. Its finite
quantum-factorial gauge has a scalar cyclic source, with the full
modified-dimension ratio retained. This resolves the norm-character
part of the generic-versus-nilpotent comparison. It does not make
the additive flow here and the geometric centralizer isomorphic.

[Exact independent audit](../experiments/audit_coherent_cut_and_ward_relative_class.py).
It passes 78 exact symbolic and cyclotomic-field checks, including
the full rational meridian variable, finite endpoint currents,
polynomial translation, and a non-covariant test of
\(L_{\mathcal E}\delta_{\mathcal E}=0\).
