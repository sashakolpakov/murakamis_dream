# Actual compact coherent composition for a capped Euler coproduct

Private written proof, 18 November 2026.

The small-activity coherent charts of the actual coproduct factors
compose on a specified compact coherent cycle. A global estimate,
including cross-pair incidence, suppresses the complement of the
identity saddle. A compact contour deformation then selects its
unique nearby critical point with a nonzero coefficient. The
exponentially small root carry transfers this result to the actual
finite polynomial of the total lowering operator.

This is a fixed-root, complete-meridian result. It neither replaces
the later quotient and turnover nor asserts that a geometric
opposite-source frame lies in its small-activity domain.

The complete directs A, C, and J are pinned below. A proves the
actual local factor kernels; C proves the capped operator comparison;
J gives the original compact resolution. The global interface bound,
adapted cycle, contour deformation, and composition coefficient are
proved here.

## 1. The actual operators and the conclusion

Fix a number \(r\ge1\) of heads, and let
\[
 N\ge2,\quad d=N-1,\quad Q=e^{2\pi i/N},\quad
 x=-e^{-\pi i/N},\qquad
 f_n=\prod_{j=1}^n(1-Q^j).
 \tag{1}
\]
The empty product is \(f_0=1\), and
\(E_N(t)=\sum_{n=0}^d t^n/f_n\).
The meridian is \(M=1\). Use the original binomial metric
\(\|w_a\|^2=\binom da^{-1}\) and the actual matrices
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad Ew_0=0,\qquad
 Kw_a=xQ^{-a}w_a.
\]
Put
\[
 X_i=E_iK_{i+1}\cdots K_r,\quad X=\sum_iX_i,\quad
 U_{i,N}(\lambda)=\sum_{n=0}^d\frac{\lambda^nX_i^n}{f_n},
 \quad
 P_N(\lambda)=U_{r,N}(\lambda)\cdots U_{1,N}(\lambda),
\]
\[
                    G_N(\lambda)=E_N(\lambda X).
 \tag{2}
\]
Every cap and Cartan factor in (2) is literal. In particular
\(X_i^N=X^N=0\).

For any fixed compact set
\[
 \mathcal K\Subset
 \mathcal X^r,\qquad
 \mathcal X=(\mathbb P^1\times\mathbb P^1)
                     \setminus\{1+wz=0\},
\]
there is a nonempty complex activity disk on which, locally in
the external coordinates,
\[
 \boxed{\quad
 \sigma_N(G_N)(\mathbf w,\mathbf z)
   =e^{N\mathcal S(\lambda,\mathbf w,\mathbf z)}
       b(\lambda,\mathbf w,\mathbf z)(1+O(N^{-1})).
 \quad}\tag{3}
\]
The phase and coefficient are holomorphic, \(b\) is a unit, and
\(\mathcal S(0)=0,\ b(0)=1\). The radius and estimates are uniform
on a finite cover of \(\mathcal K\), after shrinking the patches.
All fixed activity and external-coordinate derivatives of the
normalized error have the same order on smaller patches.
In particular the actual normalized kernel is nonzero there for
large \(N\). The normalization is exactly
\[
 \sigma_N(B)=
 \frac{v(\mathbf w)B c(\mathbf z)}
      {\prod_a(1+w_a z_a)^d},\quad
 v(w)w_a=w^a,\quad c(z)=\sum_{a=0}^d\binom daz^aw_a.
 \tag{4}
\]
The same conclusion first holds for the actual product \(P_N\);
C's retained carry then proves (3).

The argument below also applies to any fixed finite ordered list
of the factors \(U_{i,N}\), with independent sufficiently small
activities. We use a common \(\lambda\) for the coproduct in (2).

## 2. Exact adapted coherent cycles

For a finite affine external pair \((w,z)\) with \(1+wz\ne0\), set
\[
                       g=\begin{pmatrix}1&-w\\z&1\end{pmatrix}.
 \tag{5}
\]
Its first column is \((1,z)^t\), and its inverse first row is
\((1,w)/(1+wz)\). Let \(D_g=\operatorname{Sym}^d(g)\) in the
actual binomial basis. Thus
\[
 D_ge_0=c(z),\qquad v(w)D_g=(1+wz)^de_0^t.
\]
On several heads take tensor products. Consequently, exactly,
\[
                  \sigma_N(B)(\mathbf w,\mathbf z)
                        =(D_g^{-1}BD_g)_{\mathbf0,\mathbf0}.
 \tag{6}
\]
On other projective patches one first uses fixed coordinate changes
and then (5). The matrices \(g,g^{-1}\) depend holomorphically on the
chosen patch and are bounded on a smaller compact set.

Here is the actual cycle behind this identity. For one head retain
\[
 \Pi(w,z)=\frac{c(z)v(w)}{(1+wz)^d},\qquad
 \nu=-\frac{dw\wedge dz}{2\pi i(1+wz)^2},\qquad
 \Gamma=\{z=\bar w\}.
\]
J proves the exact finite resolution \(N\int_\Gamma\Pi\nu=I\).
For a general \(g=\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)\),
its action is
\[
 z\longmapsto\frac{c+ez}{a+bz},\qquad
 w\longmapsto\frac{-b+aw}{e-cw}.
 \tag{7}
\]
Direct differentiation gives
\(\nu(g(w,z))=\nu(w,z)\) and
\(\Pi(g(w,z))=D_g\Pi(w,z)D_g^{-1}\).
The identity pairing transforms by
\[
 1+w'z'=\frac{\det(g)(1+wz)}{(e-cw)(a+bz)}.
\]
Thus incidence is preserved, with all section factors accounted for.

The adapted cycle is \(\Gamma_g=g\Gamma\), with the transported
orientation. A path from the identity to \(g\) in
\(\operatorname{PGL}_2(\mathbb C)\) gives a compact homotopy in
\(\mathcal X\); such a path exists because this complex group is
connected. The cycle remains incidence-free. Hence it is homologous
to \(\Gamma\), and
\[
                       N\int_{\Gamma_g}\Pi\nu=I
 \tag{8}
\]
also follows directly by conjugation. Tensor products and repeated
resolutions retain every original finite cap. There is no
normalizing trace substitution.

Below we use standard spheres after conjugating each matrix by
\(D_g\). By (6)--(8), these are exactly the adapted cycles for the
original matrices, not an assigned saddle contour.

## 3. A global kernel bound, including cross-pair incidence

We need control where A's local nonincidence theorem cannot be used.
For homogeneous row and column vectors \(W,Z\) of Euclidean norm
one, write \(I=WZ\). The corresponding coherent row and column
have norm one in the binomial metric. Thus their matrix kernel is
bounded by the operator norm. This convention is used only for
absolute estimates; no finite cap is divided out at incidence.

For a homogeneous polynomial \(p(W_0,W_1)\) of degree \(d\), the
actual root lowering row is exactly
\[
 Ep(W)=\frac{W_0}{W_1}
             [p(W_0,Q^{-1}W_1)-p(W_0,W_1)]
 =\delta W_0\int_0^1
       (\partial_1p)(W_0,a(s)W_1)\,ds,
\]
\[
                   \delta=Q^{-1}-1,\qquad a(s)=1+s\delta.
 \tag{9}
\]
The apparent division is removable, and \(|a(s)|\le1\).
Iteration gives
\[
 E^np(W)=\delta^nW_0^n\int_{[0,1]^n}
       \left[\prod_{k=1}^n a(s_k)^{k-1}\right]
       (\partial_1^np)(W_0,\alpha W_1)\,d\mathbf s,
 \qquad \alpha=\prod_ka(s_k).
 \tag{10}
\]
This follows by differentiating successively; the derivative does
not act on \(W_0\). It includes the zero arrows because it acts on
the original degree-\(d\) polynomial space.

For \(p(W)=(WZ)^d\), the factor
\(|\delta|^n(d)_n\) is at most \((2\pi)^n\).
Also \(|\alpha-1|\le2\pi n/N\). Consequently
\[
 |K_{E^n}(W,Z)|
        \le C^n(|I|+Cn/N)^{d-n}.
 \tag{11}
\]
Under a fixed \(g\), (9)--(10) are conjugated linear coordinate
maps and linear derivative fields. Their displacement is still
\(O_g(n/N)\). The two linear factors corresponding to \(W_0^n\)
and the differentiated input coordinate cost at most \(C_g^n\).
Their nilpotent rank-one relation, which prevented derivatives
from hitting \(W_0\), is preserved by conjugation.

For \(X_i^n\), the later heads additionally have the exact rows
\((K^np)(W)=x^n p(W_0,Q^{-n}W_1)\).
The coordinate maps have displacement \(O(n/N)\), and \(|x^n|=1\).
Earlier heads retain their identity kernels. Therefore on the
standard spheres, after any fixed tensor \(g\) in a compact family,
there are constants \(C_g,\delta_0>0\) such that
\[
 |K_{D_g^{-1}X_i^nD_g}(\mathbf W,\mathbf Z)|\le C_g^n,
                         \qquad 0\le n\le\delta_0N.
 \tag{12}
\]
To obtain this bound from (11), every unseparated overlap is at
most one, and \((1+C_gn/N)^d\le e^{C_gn}\).

More strongly, if at least one head has
\[
                              |W_aZ_a|\le1-\epsilon,
 \tag{13}
\]
choose \(\delta_0\) sufficiently small in terms of
\(\epsilon,g,r\). The perturbed overlap on that head is at most
\(1-\epsilon/2\), and \(d-n\ge N/2\) for large \(N\).
The other heads cost only \(C_g^n\). Hence for some \(b>0\),
\[
 |K_{D_g^{-1}X_i^nD_g}(\mathbf W,\mathbf Z)|
                    \le C_g^n e^{-bN},
                         \qquad 0\le n\le\delta_0N.
 \tag{14}
\]
This also holds if the separated head is a spectator: its exponent
is \(d\), and decreasing it to \(d-n\) only weakens the bound.
In particular (14) includes exact cross-pair incidence \(W_aZ_a=0\).

For the low degrees use, when \(n\le N/2\),
\[
                 |f_n|\ge(4/N)^n n!.
\]
Thus (12), summed against \(|\lambda|^n/|f_n|\), is at most
\(e^{C_gN|\lambda|}\); (14) gives the same bound times \(e^{-bN}\).

For all higher degrees use an actual matrix estimate. C gives,
on a fixed small circle \(|t|=R\),
\(\|U_{i,N}(t)\|\le e^{A N R}\), since \(\|X_i\|\le\pi\).
Furthermore
\[
 \|D_g\|\|D_g^{-1}\|\le
       \prod_a(\|g_a\|\|g_a^{-1}\|)^d\le e^{\kappa_gN}.
 \tag{15}
\]
The first inequality follows by singular-value decomposition on
each two-dimensional head: the induced unitary maps preserve the
binomial metric, and the largest degree-\(d\) singular value is
\(\|g_a\|^d\). Cauchy's coefficient estimate bounds the high-degree
kernel tail by
\[
 \frac{e^{(\kappa_g+AR)N}}{1-|\lambda|/R}
           (|\lambda|/R)^{\lfloor\delta_0N\rfloor+1}.
 \tag{16}
\]
For fixed \(R,\delta_0\), its exponential rate can be made
arbitrarily negative by reducing \(|\lambda|/R\).
No individual high-degree matrix term has been omitted.

It follows that, on all independent sphere interfaces,
\[
 |K_{D_g^{-1}U_{i,N}(\lambda)D_g}|
                               \le C e^{C_gN|\lambda|},
 \tag{17}
\]
and, if (13) holds, then for sufficiently small fixed activity
\[
 |K_{D_g^{-1}U_{i,N}(\lambda)D_g}|\le C e^{-b'N}.
 \tag{18}
\]
All kernels in (12)--(18) have unit-norm coherent input and output.
Their bounds are uniform in the compact family of external frames.
The global estimate (17) has no leftover \(e^{\kappa_gN}\) cost:
that cost was confined to (16) and paid by its high-degree tail.

## 4. The exact closed interface chain and its complement

Consider \(\ell\) factors, with \(\ell\) fixed, and normalize the
external pair using (6). Insert J's exact resolutions between
them. The case \(\ell=1\) is directly A's theorem; take
\(\ell\ge2\) in the contour argument below. There are
\[
                              s=r(\ell-1)
\]
complex integration variables and an exact factor \(N^s\).
In unit coherent vectors this is simply the product of the
\(\ell\) transition kernels over the standard sphere at every
internal node. The measure is the product of the probability
measures \(\nu\). This description is valid globally, including
any zero overlap between consecutive nodes.

At zero activity, each transition kernel is the coherent overlap
to degree \(d\). Its modulus is at most one, with equality precisely
when its two projective coherent states coincide. The external
state at both ends is \(e_0\). Therefore the product has a unique
maximum of modulus one when every internal state is \(e_0\).

Fix a small neighborhood of that configuration. Outside it, some
internal head has a fixed positive projective distance from \(e_0\).
Along the finite chain from that head to an endpoint, at least one
consecutive pair has a fixed separation. This can also be seen by
compactness: the only chain with every overlap of modulus one is
the all-\(e_0\) chain. Apply (18) to one separated factor and (17)
to all others. For sufficiently small activity their product,
and its integral over this whole complement, are
\[
                                O(e^{-b''N}).
 \tag{19}
\]
The factor \(N^s\) is absorbed by slightly reducing \(b''\).
This proves a genuine global complement estimate on the exact
source chain. Cross-pair incidence was included in (18), rather
than treated as part of a nonexistent global logarithmic chart.

## 5. The actual local saddle and its coefficient

Index the internal nodes from input to output by
\(j=1,\ldots,\ell-1\). Near \(e_0\) use affine coordinates
\((w_j,z_j)\) on each head, with \(z_j=\bar w_j\) on the sphere.
Put \(w_\ell=z_0=0\). The factor connecting nodes \(j+1\) and
\(j\) has its identity pairing \(1+w_{j+1}z_j\).

A supplies on a neighborhood of this whole configuration the actual
kernel of each factor as its exact identity cap to power \(d\),
times
\(\exp(N\varphi_j)a_j(1+O(N^{-1}))\).
Here \(\varphi_j,a_j\) are holomorphic, \(a_j\) is a unit, and
\(\varphi_j(0)=0,\ a_j(0)=1\), where zero denotes activity.
Conjugation by \(D_g\) just evaluates these normalized functions
at the transformed pair. All local pairs remain nonincident.

Using \(d=N-1\), the exact local convolution integrand therefore has
phase
\[
 \Phi_\lambda=
 \sum_{j=0}^{\ell-1}\sum_a\log(1+w_{j+1,a}z_{j,a})
 -\sum_{j=1}^{\ell-1}\sum_a\log(1+w_{j,a}z_{j,a})
 +\sum_j\varphi_j,
 \tag{20}
\]
with amplitude
\[
 \mathfrak a_\lambda=
 \left(\prod_j a_j\right)
 \left(\prod_{j=0}^{\ell-1}\prod_a
                       (1+w_{j+1,a}z_{j,a})^{-1}\right)
 \left(\prod_{j=1}^{\ell-1}\prod_a
                       (1+w_{j,a}z_{j,a})^{-1}\right).
 \tag{21}
\]
The remaining volume form is
\(\prod_{j,a}[-dw_{j,a}\wedge dz_{j,a}/(2\pi i)]\),
and the external multiplier is \(N^s\).
Both inverse pairing factors in (21) are necessary: one is from
the numerator power \(d\), the other from the resolution denominator
power \(d+2=N+1\). These inverses are used only in this local chart;
the original global integrand has finite polynomial numerators.

At zero activity the critical point is zero, and the quadratic
phase on \(w_j=u_j,\ z_j=\bar u_j\) is
\[
 -\sum_j|u_j|^2+\sum_j\bar u_j u_{j+1}
                         =-u^*Bu,\qquad
 B=I-\text{upper shift},
 \tag{22}
\]
on each head. Its complex determinant is one. Separately,
\[
 \operatorname{Re}(u^*Bu)
  =\tfrac12\left(|u_1|^2+
       \sum_j|u_{j+1}-u_j|^2+|u_{\ell-1}|^2\right)>0
\]
away from zero. The determinant of this Hermitian real-part
matrix is \(\ell/2^{\ell-1}\), not one. It supplies positivity;
the complex matrix \(B\) supplies the Gaussian normalization.

The holomorphic Hessian in the independent \(w,z\) variables is
invertible. The analytic implicit-function theorem therefore
gives a unique nearby critical point \(p_\lambda=O(\lambda)\),
with holomorphic external-coordinate dependence. To place it on
an actual contour, choose a smooth cutoff supported in the small
coordinate neighborhood and equal to one near zero. Replace the
local sphere by
\[
 w=u+\chi(u)w(p_\lambda),\qquad
 z=\bar u+\chi(u)z(p_\lambda).
 \tag{23}
\]
Multiplying the displacement by a real parameter in \([0,1]\)
gives a compact homotopy, equal to the old cycle outside the chart.
For small activity it avoids every diagonal incidence divisor.
All integrands are holomorphic top forms there; Stokes therefore
preserves the exact finite integral. No new boundary or infinity
chain is suppressed.

Near the critical point, (23) is a translation of the old tangent
plane. Positivity in (22) persists under a sufficiently small complex
activity perturbation. On the cutoff annulus the strict identity
gap also persists, since the local phase and the displacement change
by \(O(|\lambda|)\). Outside this chart the global estimate (19)
continues to apply on the unchanged cycle. Reducing the activity
radius once more makes both complements exponentially subordinate
to the critical value
\[
                      \mathcal S(\lambda)=\Phi_\lambda(p_\lambda),
                          \qquad \mathcal S(0)=0 .
 \tag{24}
\]
Here \(|\operatorname{Re}\mathcal S|\le C|\lambda|\).

Finite-dimensional Gaussian expansion on the translated local
plane now yields
\[
                     \sigma_N(P_N)
       =e^{N\mathcal S}b(1+O(N^{-1})),
 \tag{25}
\]
with a holomorphic nonzero coefficient \(b\).
For clarity, let \(H_\lambda\) be minus the Hessian of
\(\Phi_\lambda\) in the \(2s\) real coordinates of the translated
plane, viewed as a complex symmetric matrix. Its real part is
positive definite. The amplitude is explicitly
\[
 b=\mathfrak a_\lambda(p_\lambda)
                   \sqrt{\frac{\det H_0}{\det H_\lambda}},
 \tag{26}
\]
with the square root continued from one at zero activity.
No contour-orientation sign is left unspecified.

Indeed at zero activity
\[
 \int_{\mathbb C^s}e^{-N u^*(B\otimes I_r)u}
                     \prod_\alpha\frac{d^2u_\alpha}{\pi}
                                   =N^{-s}.
 \tag{27}
\]
One direct proof expands the upper-shift exponential. Its absolute
series is dominated by a Gaussian because the real Dirichlet form
is positive. Each nonconstant monomial has an unbalanced angular
charge at an endpoint of its finite directed chain, so its angular
integral vanishes. Only the constant term remains, proving (27).
The local orientation is
\(-du\wedge d\bar u/(2\pi i)=d^2u/\pi\).
Thus \(N^s\) cancels exactly, and (21) gives \(b(0)=1\).
Holomorphic continuation of the Gaussian gives (26).

For the error estimate, split a small translated real neighborhood
at radius \(N^{-2/5}\). The outside has a strict Gaussian gap;
inside, Taylor expansion through cubic phase and linear amplitude
has vanishing odd Gaussian terms. The remaining Gaussian moments
give relative \(O(N^{-1})\). A's finite relative errors have the
same order, since the number of factors is fixed. All bounds hold
on enlarged compact parameter sets; Cauchy estimates give fixed
derivatives of the normalized error. For \(\ell=1\) there are no
integration variables, and (25) is directly A's theorem.

This proves (25) from the actual compact finite convolution,
not from a formal composition of generating functions alone.

## 6. Transfer to the total operator and scope

For the ordered product in (2), C gives
\[
 \sup_{\mathcal K}|\sigma_N(P_N-G_N)|=O(e^{-\Lambda N})
 \tag{28}
\]
with any prescribed fixed \(\Lambda>0\), after reducing the activity
disk. This comparison includes the original coherent conditioning
cost. Since \(\mathcal S=O(\lambda)\) and \(b\) is a unit, choose
the disk so that (28) is exponentially small relative to the
actual leading term in (25). Equations (25),(28) prove (3).

The normalized phase in (24) is obtained from the stationary
composition of A's actual local factor phases, with the external
identity cap divided out as in (4). Its branch and coefficient are
fixed by the identity kernel. All internal stationary rows, finite
caps, Cartan half-steps, and \(N-1\) corrections were included in
(20)--(21). The full unnormalized phase is
\(\sum_a\log(1+w_az_a)+\mathcal S\); near zero activity its boundary
mixed Hessian is that of the identity graph up to a small
perturbation. This is an actual regular
local generating kernel, not an assertion that a prescribed
loxodromic geometric point is in its activity domain.

The proof is at \(M=1\). It may be differentiated in activity and
external coherent coordinates as stated. It is not differentiated
in the meridian or the quantum parameter. In particular
\[
 E(M)=M E(1)+(M-M^{-1})L,\qquad
 Lp=W_0\int_0^1(\partial_1p)(W_0,sW_1)\,ds
\]
contains a whole radial path, unlike the \(O(N^{-1})\) path in (9).
A meridian-normal vacuum term therefore cannot be assigned the
separated-link estimate merely by differentiating the root proof.
Shifted denominators also retain their own normal insertions.

Finally the later quotient \(q_F\), balanced turnover, source
normalization, and relative-window currents of J are not removed
by (3). Their composition needs its own interfaces and estimates.
No geometric-cycle coefficient or nonzero closed-source period is
deduced from this actual coproduct-factor chart.

## Complete proof directs

* A: notes/research_actual_coupled_euler_coherent_flow.md,
  SHA256 a7d3d29f4381f669fd3f6e72a6c637fa259e650757bd39a517e47c0419692def.
* C: notes/research_root_capped_euler_coproduct_factorization.md,
  SHA256 e11f5f827f226ee93505e00aed3885a33abdbfc15ee71e023a67c048c9c17720.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

All three complete directs were freshly read nontruncated in this
active author sequence and retained unchanged. The matching entire
final was read back, every used implication checked, and all four
hashes renewed before freezing. Only written mathematics and
text/hash operations were used. Frozen and public files were unchanged.

