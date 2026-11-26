# A common orthogonal basis for coherent crossing amplitudes

24 November 2026. Research note. Written proof.

For fixed actual neighboring heights, one real symmetric Jacobi matrix
handles every input label in the cooriented crossing block. Its orthogonal
basis is independent of that input. Consequently the actual sum over
inputs is an exact finite Cauchy transform in each output mode, and its
full cross-input Gram is a divided difference of a matrix resolvent.
Here coherent means that the input sum is taken before an absolute square.

These are exact finite source identities. The complementary input can
contribute to the same output modes and remains inside those squares.
Neither positivity of the Gram nor polynomial conditioning of the Jacobi
matrix gives injectivity or a polynomial lower bound for that input map.

## 1. Fixed source domains without ordering the middle labels

Use the complete conventions of G,H,N,T:
\[
 N\ge2,\quad q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad
 \delta=\pi/N,\quad \sqrt q=e^{\pi i/(2N)},\quad
 \lambda_r=2\sqrt q\cos\alpha_r,\quad
 \alpha_r=(r+\tfrac12)\delta,\quad\mu_r=\sin\alpha_r.
 \tag{1}
\]
All indices are between zero and d. Write J(r,t;v,s) for G's actual
phase-removed mixed-continuant coefficient. Fix the two physical neighbor
indices (v,s), put S=max(v,s), T_0=N-S-2, and let
\(\mathcal C=\{0,\ldots,T_0\}\). If T_0<0 this set is empty and
the whole physical block is retained literally. Otherwise put
\[
 a=\max(\cos\alpha_v,\cos\alpha_s),\quad
 b=\min(\cos\alpha_v,\cos\alpha_s)=\cos\alpha_S,\quad
 x_t=\cos\alpha_t,\quad y_r=\cos\alpha_r .
 \tag{2}
\]
This is numerical ordering of two scalars. No physical neighbor swap
or symmetry of a complementary block is asserted. G's amplitude symmetry
allows its wall formula to use this S with the original (v,s).

The source recurrence, algebraically valid for every input r, is
\[
 c_t^+J(r,t+2)+d_tJ(r,t)+c_t^-J(r,t-2)=2y_rJ(r,t),
\]
\[
 c_t^\pm={(\cos(\alpha_t\pm\delta)+a)
 (\cos(\alpha_t\pm\delta)+b)\over
 \sin\alpha_t\sin(\alpha_t\pm\delta)},\qquad
 d_t={-2[x_t(1+ab)+(a+b)\cos\delta]\over
                       \sin^2\alpha_t-\sin^2\delta}.
 \tag{3}
\]
It follows from N's finite cyclic relation and T's actual crossing
intertwining, as derived in G. It is not restricted to r<=t.
The positivity bound also needs no such ordering. Write
c_delta=cos(delta), L_0=-cos((S+3/2)delta),
u_0=c_delta+L_0 and K_0=(1-a)(1-b).
For all \(r,t\in\mathcal C\), x_t,y_r>=L_0 and u_0>1-b.
Therefore the row defect on every used interior row obeys
\[
 \omega_t(r)=2\left[y_r+c_\delta-{K_0\over c_\delta+x_t}\right]
 \ge2\left[u_0-{(1-b)^2\over u_0}\right]
 \ge4\sin(\delta/2)[\sin((S+1)\delta)-\sin(\delta/2)]
 \ge cN^{-2}.
 \tag{4}
\]
Here u_0-(1-b)=2sin(delta/2)[sin((S+1)delta)-sin(delta/2)].
Every edge coefficient used in the interiors I_p or their incident
Dirichlet boundaries is positive and bounded by CN^2.

For p=0,1 with p<=T_0 define the fixed interior
\(I_p=\{p+2,p+4,\ldots\}\cap\mathcal C\).
Keep the literal lower output row t=p. If the last interior is T_0,
its outgoing coefficient is exactly zero. If it is T_0-1, retain the
literal wall row u=T_0+1. The latter coefficient J(r,u;v,s) is the
calibrated wall value proved in G, for every \(r\in\mathcal C\).
Boundary couplings are always taken from the incident interior row.
Equation (3) is used only on these interior output rows; it is valid
for every input r. The lower rows p=0,1 remain literal boundary rows.
For S=0 the possible terminal row t=N-2 has its upper folded edge killed
by the actual source cut in N; (3) is used with that term omitted.
Empty interiors require no recurrence or inverse. This includes every
cooriented block at N=2,3 and the cases T_0=0,1.

## 2. One input-independent symmetric matrix

For a nonempty I_p, let L_p be (3) on I_p, omitting boundary terms from
its matrix but keeping the original diagonal d_t. Put
D_p=diag(sqrt(mu_t)) on I_p and
\[
 y_*=\cos\alpha_{T_0},\quad
 A_p=D_p(2y_*I-L_p)D_p^{-1},\qquad
 \tau_r=2(y_r-y_*)\ge0\quad(r\in\mathcal C).
 \tag{5}
\]
Detailed balance is exact:
\(\mu_tc_t^+=\mu_{t+2}c_{t+2}^-\).
Thus A_p is real symmetric. More explicitly, with w=D_p^{-1}z,
\[
 \begin{split}
 z^*(A_p+\tau_rI)z={}&
 \sum_{\text{internal edges}}\mu_tc_t^+|w_{t+2}-w_t|^2\\
 &+\sum_{\text{boundary exits}}\mu_tc_{\rm exit}|w_t|^2
   +\sum_{t\in I_p}\mu_t\omega_t(r)|w_t|^2 .
 \end{split}
\]
Boundary coefficients are taken from the incident interior rows.
Formula (4) therefore gives
\[
 cN^{-2}I\le A_p+\tau_rI\le CN^2I,\qquad 0\le\tau_r\le4.
 \tag{6}
\]
For the lower bound the displayed form is at least
sum omega_t(r)|z_t|^2. For the upper bound the off-diagonal entries
are minus sqrt(c_t^+c_{t+2}^-), and the diagonal is bounded by CN^2.
These bounds include A_p itself and give condition at most CN^4.

Choose a real orthogonal O_p with
\(O_p^TA_pO_p=\operatorname{diag}(\kappa_1,\ldots,\kappa_m)\).
It can be fixed canonically: order eigenvalues increasingly and choose
each eigenvector's first coordinate positive. A nonempty irreducible
Jacobi path has simple eigenvalues and no eigenvector with first
coordinate zero, since its first row and recurrence determine all
coordinates. The one-dimensional case uses O_p=1. Thus this is a finite
algebraic choice depending on N and the actual neighbors, not on r or
on a completed-word coefficient.

Let b_L have its only nonzero entry sqrt(mu_first)c_first^-.
On a wall branch let b_R have its only nonzero entry
sqrt(mu_last)c_last^+; omit it on a natural branch. Set
\[
 B_p=(b_L\ b_R),\quad
 \rho_r=\sqrt{\mu_r}\binom{J(r,p;v,s)}{J(r,u;v,s)},\quad
 K_{tr}=\sqrt{\mu_t\mu_r}\,J(r,t;v,s),\quad
                          t\in I_p,\ r\in\mathcal C,
 \tag{7}
\]
with just the first column and first component on a natural branch.
All entries of rho are original finite source boundary values. The exact
crossing recurrence now reads
\[
 (A_p+\tau_rI)K_{\bullet r}=B_p\rho_r,\qquad
 A_pK+K\operatorname{diag}(\tau_r)=B_p(\rho_r)_r .
 \tag{8}
\]
The right side has rank at most two. This is the actual finite
Sylvester displacement relation for the cooriented crossing rectangle.

## 3. Coherent sums and the cooriented block's Gram

Write R_p(s)=(A_p+sI)^{-1}. For any complex input vector xi on
\(\mathcal C\), (8) gives, in the one fixed output basis,
\[
 (O_p^TK\xi)_k
    =\sum_{r\in\mathcal C}
       {(O_p^TB_p\rho_r)_k\over\kappa_k+\tau_r}\,\xi_r,\qquad
 \|K\xi\|^2=\sum_k\left|
     \sum_{r\in\mathcal C}{(O_p^TB_p\rho_r)_k\xi_r
                                  \over\kappa_k+\tau_r}\right|^2.
 \tag{9}
\]
The input sum is inside each square. Orthogonality does not replace it
by a sum of column energies. The modes and boundary vectors can have
signs, and xi can be complex.

The entire Gram between different inputs also has an exact small response
formula. For real s>=0 put
\[
 W_p(s)=B_p^TR_p(s)B_p,\qquad
 \mathcal L_p(s,t)=
 \begin{cases}[W_p(s)-W_p(t)]/(t-s),&s\ne t,\\-W_p'(s),&s=t.
 \end{cases}
 \tag{10}
\]
Resolvent multiplication gives
\[
 \mathcal L_p(s,t)=B_p^TR_p(s)R_p(t)B_p,\qquad
 (K^\dagger K)_{rq}=\rho_r^T\mathcal L_p(\tau_r,\tau_q)\rho_q .
 \tag{11}
\]
These formulas include coincident shifts without subtractive ambiguity.
The matrix-valued kernel is positive semidefinite: for arbitrary real
s_r>=0 and complex vectors h_r of the boundary dimension,
\[
 \sum_{r,q}h_r^*\mathcal L_p(s_r,s_q)h_q
              =\left\|\sum_rR_p(s_r)B_ph_r\right\|^2\ge0 .
 \tag{12}
\]
Rank at most two applies to the forcing in (8), not to K or its Gram.
The literal output rows p=0,1 that lie in \(\mathcal C\) remain separate.
Their entries are sqrt(mu_p mu_r)J(r,p); add their rank-one row Grams to
(11), and sum over the disjoint interior parities. This gives the
complete Gram of the cooriented rectangle, including every cross-input
term. Empty interiors contribute no resolvent term.

W_p is a finite rational response of this specified Jacobi matrix.
Its poles are the negative eigenvalues -kappa_k. This is not asserted
to be a peripheral parameter or an off-grid continuation of the entire
original quantum source. The uniform condition of A_p does not imply
injectivity or polynomial conditioning of K, its input Gram, or a
coherent scalar observation.

## 4. The actual metric, phases and the complementary input

Use H's absolute-height metric G_ht, not T's physical joint Haar form.
In its globally orthonormal nested height coordinates, G and H give
\[
 \widetilde B^\epsilon_{tr}
  =(f_vf_s)^\epsilon\,(-1)^t f_t^{-\epsilon}
       \sqrt{\mu_t\mu_r}\,J(r,t;v,s)f_r^{-\epsilon},\quad
 f_r=e^{i\pi r(r+1)/(4N)},\quad\epsilon=\pm1,
 \tag{13}
\]
for the cooriented rectangle. The original scalar is included:
\(\kappa=q^{d^2/2}\) and \(\kappa q^{d/2}i^{-d}=1\).
There are no neighboring h_N volume corrections in this metric.
All diagonal chirps displayed in (13) are unitary; their removal is
only a change of coordinates, not a replacement of signed coefficients
by positive ones.

For each actual fixed (v,s) sector, extend the real O_p on its interiors
by identity on its literal boundary rows and on t outside \(\mathcal C\).
Together these blocks define one full conditional unitary O_ext.
Keep the separate known diagonal phase matrices on all heights, even
where (13)'s positive amplitude assertion is not used. The complete
output basis change is V=P_epsilon O_ext, where P_epsilon has diagonal
(-1)^t f_t^{-epsilon}. It is unitary in G_ht and preserves the full
finite dimension.

In particular the physical input need not lie in \(\mathcal C\).
Split it only for bookkeeping as a=a_C+a_Q. In an interior output mode
the full transformed output is
\[
 [V^\dagger\widetilde B^\epsilon a]_k
   =(f_vf_s)^\epsilon[O_p^TK\xi]_k
       +[V^\dagger\widetilde B^\epsilon a_Q]_k,\qquad
                         \xi_r=f_r^{-\epsilon}(a_C)_r .
 \tag{14}
\]
Both terms remain inside the same absolute square. The boundary output
rows and the complementary output rows are retained literally as well.
There is no orthogonal separation by input support, and no discarded
leakage block. Nor is symmetry of any complementary physical block
inferred by numerically ordering a,b.

## 5. Exact sewing and its limits

These full conditional unitaries may be used as coordinate changes at
arbitrary stages of an actual finite composition. Interfaces are products
of the neighboring full basis changes and hence are unitary, even for
overlapping faces. They are retained as operators; they need not be the
identity or preserve the diagonal Cauchy variables of the next crossing.
For a full basis change V, the input becomes V^dagger u, the literal
closing row becomes ell V, and any source constraint or projector P
becomes V^dagger P V. No commutation or invariance of P is asserted.
Thus the original scalar, marked position and external factor chi_N
are unchanged. The source and cap norms already proved in H are
unchanged in G_ht. All Casimir-normal data remain in these invertible
full changes; no value-only quotient or source projection is inserted.

This is not a claim that the braid operators themselves are unitary,
or that G_ht is the physical Hilbert metric. It gives no additive
rank bound for a whole word: consecutive Jacobi generators and their
conditional bases depend on different neighboring heights. The exact
cross-input Gram and the transformed marked row may still have a small
or zero coherent overlap. No phase alignment, geometric cycle, global
closed-scalar lower bound or arbitrary-short-filling theorem follows.

J already treats a different original Newton-value Jacobi problem,
its Fourier image and the distinct normal-weighted final observation.
The abstract spectral theorem, resolvent identity and positive Gram
identity are standard finite linear algebra. The additional content
here is their exact common-output realization for all inputs of this
coideal crossing rectangle, with the rank-at-most-two source forcing,
full cross-input terms and literal source/closing transport. It does
not replace the original global minimization by independent column
energies.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| G | [All cooriented amplitudes](research_coideal_cooriented_volume_kernel.md) | 613 | 78fabcccdd4eb8e2bf4064ec281880cc551443d2d36eb72750f27c77506bd597 |
| H | [Height pairing and marked boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| N | [Actual coideal difference equation](research_coideal_marked_boundary_normal_gap.md) | 512 | bb9bd6d04480ae8733c0fd1c5901834bdf2ea3e8c7eb3617fb8eb58e66e57956 |
| T | [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| J | [Earlier physical Jacobi boundary](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md) | 432 | 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583 |

Only written mathematics, complete source reads and text/hash operations
were used. Earlier final notes, the ledger and public manuscripts remain unchanged.
