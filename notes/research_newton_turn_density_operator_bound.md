# A polynomial Newton operator bound for the original turn-trace density

Written proof, 24 November 2026. Earlier finals and public
manuscripts are unchanged.

The original diagonal turn kernel provides a canonical weight for
the full-primary compression of the genuine turn. Every selected
compression is invertible, with inverse norm at most \(m(N+2)\)
when \(m\) distinct Casimir nodes are retained. This holds for every
cluster size and includes both directions at each double root.

For the whole algebra it gives a polynomial operator bound for the
original turn-trace density. Its known small nodal weights and
indefinite signature remain; no positive scalar closing or geometric
lower bound is inferred.

## 1. Original algebra, turn and density

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(\eta=(-1)^d\).
Use the full original algebra and normalized Newton basis [A,T]:
\[
 {\cal A}_N=\mathbb C[z]/P_N(z),\qquad P_N(z)=2T_N(z/2)+2,
 \qquad c_j=2\cos((2j+1)\pi/N),
\]
\[
 S_0=1,\qquad S_r=\prod_{h=1}^r2\sin(\pi h/N),\qquad
 b_r(z)=S_r^{-2}\prod_{j<r}(c_j-z),\quad 0\le r\le d.       \tag{1}
\]
Here \(T_N\) is Chebyshev of the first kind. Newton coefficients
carry their usual positive Hermitian norm. The basis polynomials
are real. All first normals at double roots remain independent.
The original turn and cylindrical closing satisfy
\[
 {\cal T}b_r=b_{d-r},\quad {\cal T}^*={\cal T}={\cal T}^{-1},
 \qquad \phi(f)=\eta N^2[z^d]\operatorname{rem}_{P_N}f,
 \qquad \phi(b_rb_s)=\delta_{r+s,d}.                       \tag{2}
\]
Thus \(\phi(fg)=f^{\mathsf T}{\cal T}g\) on coefficient vectors.
The other original row is \(\lambda_0=\phi{\cal T}\).
No ordinary cap is substituted for the prescribed mark.

Write \(Z=M_z\). The Newton product recurrence gives
\[
 Zb_r=c_rb_r-4\sin^2(\pi(r+1)/N)b_{r+1}\quad(r<d),
 \qquad Zb_d=c_db_d,\qquad \|Z\|\le6.                      \tag{3}
\]
The faithful full minimal polynomial is \(P_N\).

Define the literal diagonal kernel and its canonical quotient inverse:
\[
 {\cal B}_N(z)=\sum_{r=0}^d b_r(z)^2,\qquad
 \mathfrak b_N={\cal B}_N^{-1}\ \text{in }{\cal A}_N.       \tag{4}
\]
Since \({\cal B}_N(x)\ge1\) on the real axis, it is a unit in
the full repeated-root algebra. The inverse retains its prescribed
first derivatives, not only its distinct-root values. The existing
turn-trace theorem [T] proves the exact original-source identity
\[
 \phi(f)=\operatorname{Tr}({\cal D}_N M_f),\qquad
                 {\cal D}_N={\cal T}M_{\mathfrak b_N}.    \tag{5}
\]
The trace acts on the \(N\)-dimensional Newton algebra.
All original framing and external factors remain attached to the
original source when (5) is used.

## 2. Full-primary Newton frames and their source normalization

The distinct double nodes are indexed by
\(0\le i\le\lfloor(N-2)/2\rfloor\). There is one additional simple
node \(-2\) at odd levels. Let \({\cal I}_i\) be its full primary ideal,
of dimension two or one respectively.

For a double node \(c=c_i\), put
\[
 a_i=\eta(4-c^2),\qquad \chi_i=\frac{c}{4-c^2},\qquad
 v_i=(b_r(c))_{r=0}^d,\quad w_i=(b_r'(c))_{r=0}^d,
\]
\[
 A_i=\|v_i\|^2={\cal B}_N(c),\qquad
 \alpha_i=\frac{v_i^{\mathsf T}w_i}{A_i},\qquad
 \delta_i=\frac{\|w_i-\alpha_iv_i\|}{\sqrt{A_i}}.          \tag{6}
\]
These are real Newton coordinate vectors and a real positive
normal scale, not magnetic Clebsch columns in a physical pair degree.

The local source coefficients can be checked directly.
The Chebyshev equation is
\[
 (4-z^2)P_N''-zP_N'+N^2(P_N-2)=0.
\]
For \(Q_i=P_N/(z-c)^2\), this equation and its derivative give
\[
 Q_i(c)=\frac{N^2}{4-c^2},\qquad
 \frac{Q_i'(c)}{Q_i(c)}=\frac{c}{4-c^2}.
\]
The original residue \(\eta N^2\operatorname{Res}(h/P_N)\)
at \(c\) is therefore
\[
                    a_i h'(c)-\eta c\,h(c).              \tag{7}
\]
At the odd simple node, \(P_N'(-2)=N^2\), so its residue is \(h(-2)\).

Let \(p_i\) be the full primary idempotent and
\(n_i=(z-c_i)p_i\). Testing (7) on an arbitrary original spectator,
and using the nondegenerate pairing (2), proves
\[
 n_i=a_i{\cal T}v_i,\qquad
 p_i={\cal T}(-\eta c_i v_i+a_iw_i).                       \tag{8}
\]
These identities prove that the following frame spans the entire
actual primary ideal:
\[
 E_i=\left(\frac{{\cal T}v_i}{\sqrt{A_i}},
       \frac{{\cal T}(w_i-\alpha_iv_i)}
                         {\sqrt{A_i}\delta_i}\right),\qquad
 E_i^{\mathsf T}E_i=I_2,
 \qquad
 ZE_i=E_i\begin{pmatrix}c_i&\delta_i^{-1}\\0&c_i\end{pmatrix}.
                                                                  \tag{9}
\]
In particular \(\delta_i>0\). The first vector is the nilpotent
eigenvector direction; the second retains the generalized direction.
The Jordan identity follows from
\((Z-c_i)p_i=n_i\), not from differentiating a root-only equality.

At the odd simple node define \(v_i=(b_r(-2))_r\),
\(A_i=\|v_i\|^2\), and \(E_i={\cal T}v_i/\sqrt{A_i}\).
Its primary idempotent is \({\cal T}v_i\). Distinct primary ideals
have zero product, hence
\[
                     E_i^{\mathsf T}{\cal T}E_j=0
                              \qquad(i\ne j).             \tag{10}
\]
All frames are real, so their transpose here is also their
Hermitian adjoint. This is full-primary Frobenius orthogonality,
not Hermitian orthogonality between the primary ideals themselves.

Two existing kernel estimates control the scales in (6).
Writing \(K_N(z,w)=\sum_r b_r(z)b_r(w)\), one has
\[
 \delta_i^2=
   \left.\partial_z\partial_w\log K_N(z,w)\right|_{(c_i,c_i)}.
\]
The all-color first-normal theorem [H, Theorem 1] gives
\[
 \frac18\le\delta_i\le\gamma_i,\qquad
 \gamma_i=\frac{N-2i-1}{4\sin\theta_i},\qquad
 \theta_i=(2i+1)\pi/N.                                    \tag{11}
\]
The lower bound follows separately from (3),(9):
\(\delta_i^{-1}\le\|Z-c_i\|\le8\).
The diagonal-kernel derivative bound [T, (12)] also gives
\[
             -N^2/8\le\alpha_i\le0,\qquad
             {\cal B}_N'(c_i)=2A_i\alpha_i.               \tag{12}
\]

## 3. Canonical weighted turn blocks

Formula (7) applied to (8),(9) yields
\[
 E_i^{\mathsf T}{\cal T}E_i
 =\frac1{a_iA_i\delta_i}
       \begin{pmatrix}0&1\\1&(\chi_i-2\alpha_i)/\delta_i\end{pmatrix}.
                                                                  \tag{13}
\]
The original diagonal kernel, including its first normal (12), acts by
\[
 M_{{\cal B}_N}E_i
 =E_i A_i\begin{pmatrix}1&2\alpha_i/\delta_i\\0&1\end{pmatrix}.
\]
Consequently its shear cancels exactly:
\[
 C_i:=E_i^{\mathsf T}{\cal T}M_{{\cal B}_N}E_i
 =\frac1{a_i\delta_i}
             \begin{pmatrix}0&1\\1&\chi_i/\delta_i\end{pmatrix},
 \qquad
 C_i^{-1}=\begin{pmatrix}-a_i\chi_i&a_i\delta_i\\
                                     a_i\delta_i&0\end{pmatrix}.
                                                                  \tag{14}
\]
This uses the canonical source kernel \({\cal B}_N\), not a scalar
replacement of its jets. Omitting its derivative would leave the
\(\alpha_i\) term in (13).

Now \(a_i\chi_i=\eta c_i\), and (11) gives
\[
 |a_i\delta_i|
 \le4\sin^2\theta_i\,\gamma_i
 =(N-2i-1)\sin\theta_i\le N .
\]
Splitting the last matrix in (14) into its diagonal and off-diagonal
parts proves the universal bound
\[
                         \|C_i^{-1}\|\le N+2.             \tag{15}
\]
At the odd simple node the same weighted block is exactly \(C_i=1\).
Cross blocks in (14) vanish for distinct nodes, since multiplication
by \({\cal B}_N\) preserves each full primary ideal.

## 4. Every selected compression and the global density bound

Select any nonempty set \(J\) of \(m\) distinct nodes, keeping each
full primary ideal. Set
\[
 {\cal I}_J=\bigoplus_{i\in J}{\cal I}_i,\quad
 V=(E_i)_{i\in J},\quad G=V^{\mathsf T}V>0,\quad
 C=\operatorname{diag}_{i\in J}(C_i).
\]
Primary decomposition proves that \(V\) has full column rank.
Its individual blocks are orthonormal, so
\(\|V\|^2\le m\), without a lower Gram bound.
Let \(P_J=VG^{-1}V^{\mathsf T}\) be the Newton orthogonal projection
onto this selected sum and define its measured weighted turn by
\[
              H_J=P_J{\cal T}M_{{\cal B}_N}|_{{\cal I}_J}. \tag{16}
\]
For every coefficient vector \(x\),
\(H_J(Vx)=VG^{-1}Cx\). Hence the inverse on the selected sum is
\[
 H_J^{-1}=VC^{-1}V^{\mathsf T}|_{{\cal I}_J},\qquad
 \boxed{\quad \|H_J^{-1}\|\le m(N+2),\qquad
 \|H_Ju\|\ge\frac{\|u\|}{m(N+2)}.\quad}                    \tag{17}
\]
Multiplying both displayed maps on \(Vx\) verifies both inverse
identities. This argument needs no sublinear restriction, no estimate
on \(\|G^{-1}\|\), and no ambient spectral-projector bound.

For all \(q_N=\lceil N/2\rceil\) distinct nodes, the selected sum is
the whole algebra. Then \(P_J=I\), and
\[
 ({\cal T}M_{{\cal B}_N})^{-1}
      =M_{\mathfrak b_N}{\cal T}
      =V\operatorname{diag}(C_i^{-1})V^{\mathsf T}.
\]
The order of these factors matters. The original density in (5) is
\({\cal D}_N={\cal T}({\cal T}M_{{\cal B}_N})^{-1}{\cal T}\),
not the inverse itself. Since the turn is unitary,
\[
 \boxed{\quad
 \|M_{\mathfrak b_N}\|_{{\rm Newt}\to{\rm Newt}}
   =\|{\cal D}_N\|
   \le\lceil N/2\rceil(N+2).
 \quad}                                                   \tag{18}
\]
This is an operator estimate on the entire original Newton algebra,
including arbitrary coherent inputs and every first normal.
It strengthens the earlier pointwise and real-boundary estimates
for \(\mathfrak b_N\); it does not bound its inverse polynomially.

For a fixed number \(r\) of contracted algebra copies, [T, (9)] gives
\(\phi^{\otimes r}(F)=\operatorname{Tr}({\cal D}_N^{\otimes r}M_F)\).
Put \(C_N^{\rm dens}=\lceil N/2\rceil(N+2)\). For every operator error \(\Delta A\)
on that full tensor algebra, with \(\|A\|_1=\operatorname{Tr}\sqrt{A^*A}\),
one has
\[
 |\operatorname{Tr}({\cal D}_N^{\otimes r}\Delta A)|
 \le(C_N^{\rm dens})^r\|\Delta A\|_1
 \le(C_N^{\rm dens})^rN^r\|\Delta A\|_{\rm op}.          \tag{18a}
\]
This is polynomial absolute source error with the actual density retained in the leading trace, not a relative scalar estimate.

## 5. The original closing under the canonical half-density

The original cylindrical row on each paired frame is exactly
\[
             \phi E_i=A_i^{-1/2}(1,-\alpha_i/\delta_i).    \tag{19}
\]
Indeed \(\phi({\cal T}v_i)=b_0(c_i)=1\) and
\(\phi({\cal T}w_i)=b_0'(c_i)=0\). At the odd simple node the row is
\(A_i^{-1/2}\).

Let \(s_N\) be the real Hermite unit with \(s_N^2={\cal B}_N\) and
positive nodal values. Its full prescribed jets are
\(s_N(c_i)=\sqrt{A_i}\) and
\(s_N'(c_i)=\sqrt{A_i}\alpha_i\) at double nodes; at the simple
node only its value is prescribed. This is the inverse of the
positive-jet square root of \(\mathfrak b_N\) used in [T].
Thus
\[
 M_{s_N}E_i=E_i\sqrt{A_i}
              \begin{pmatrix}1&\alpha_i/\delta_i\\0&1\end{pmatrix},
 \qquad
                  \phi M_{s_N}E_i=(1,0).                 \tag{20}
\]
The simple block gives \(\phi M_{s_N}E_i=1\).
This identifies the original row in a specified full-normal frame.
Its kernel remains: (20) is not a scalar lower bound for an arbitrary
incoming packet. The unweighted source is restored with \(M_{s_N}^{-1}\);
neither its action factor nor the original mark has been removed.

## 6. Scope and complete sources

The weight in (14)--(18) is the actual diagonal kernel from the
original turn-trace source. A double block has negative determinant.
Also \({\cal D}_N\) is real symmetric, invertible, and has trace
\(\phi(1)=0\), hence is indefinite. The operator upper bound (18)
does not turn its original trace pairing into a positive norm.

The original nodal weights \(\mathfrak b_N(c_i)\) can still be exponentially
small at central nodes, as [T] proves. No lower bound for the smallest
singular value of \({\cal D}_N\), an arbitrary original closing, or geometric coefficient
is inferred. Nor is inserting \(P_J\) into a closed source authorized
by (17): its omitted component and subsequent exterior remain.
Actual turns, pivots, crossing phases and prescribed source rows
retain their original meanings.

The closest physical middle-weight turn theorem [M] already gives
an exact kernel and positive transported boundary Gram. Its flat
physical coordinates and positive-metric transport are different
from the full-primary Newton compression considered here.
There is no new interpolation or abstract compression method claimed.
The new estimates are (17)--(18) for the canonical original-source
density, with the explicit normal and closing calibrations above.
No new knot-volume or finite-exception theorem is proved.

The following complete matching source texts were read:

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| A | [Newton turn and original rows](actual_newton_turn_positive_gram.md) | 434 | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| H | [All-color first-normal bound](research_all_color_path_normal_bound.md) | 671 | 08f8932c2cdee4c7afadbb4db3cd85480603f8adb4c936ce29a5517b2d4799c7 |
| T | [Original turn-trace density](research_turn_trace_residue_density.md) | 335 | 48c31b23c3c8f5c2245dcd585e8012637bbbaed63dfc2c9405c70d42e9960293 |
| M | [Closest physical middle-weight turn](research_middle_weight_turn_gram_kernel.md) | 442 | 01f2c9d5724eca87c6bef1ffa8a6faae53f47d5dbdc7e71513165c39cb674e41 |

Only written mathematics, complete text reads and metadata operations
were used. No mathematical program, numerical test, build, git
operation or earlier-final/public-manuscript edit was performed.
