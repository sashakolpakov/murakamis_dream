# The actual weighted Ward boundary and its local coarea adapter

Private written proof, 18 November 2026.

The complete cut/pivot boundary of the weighted Ward current has
three explicit finite coupons. They are derivatives of a literal
second-quantized cut matrix. This gives a local parameter-dependent
Borel/coarea realization of the corresponding ordinary-color source,
including the original soft endpoint and every upper cutoff jet.

The finite-root identity and the ordinary-color analytic family are
distinguished throughout. No equality between a summed \(q=1\) family
and the whole fixed-level meridian germ is inferred. No transport from
the central highest-cut augmentation to a noncentral parabolic frame,
or lower bound for the physical scalar, is claimed.

## 1. The entire finite boundary cofactor

Use [W]'s literal factorial basis and conventions:
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad h=2\pi i/N,\quad x=-M/q,
 \quad N\ge2,\quad M\ne0.
 \tag{1}
\]
Write \(E=\mathcal E\), and let \(E_B,F_B,K_B\) be the iterated
coproduct on heads \(2,\ldots,b\). Set
\[
 g_B=K_B^{1-N},\quad P=T_0\otimes g_B,\quad
 \epsilon=MQ^{-1}-M^{-1},\quad \eta=1-Q.
 \tag{2}
\]
For \(b=1\), the tail is the scalar space and \(F_B=0\).
The total generators and the ordered coefficients of [W] satisfy
\[
 E_*=E_1K_B+E_B,\qquad
 F_*=F_1+K_1^{-1}F_B,\qquad K_*=K_1K_B,
\]
\[
 A_E=Q^{-1}F_1K_B^{-1},\qquad A_F=E_1,\qquad [P,K_*]=0.
 \tag{3}
\]
The first identity for \(A_E\) follows from
\(A_E=K_1F_1K_*^{-1}\) and \(K_1F_1K_1^{-1}=Q^{-1}F_1\);
it does not commute an arbitrary weight through a generator.

Define the cofactor, including its \(h^{-1}\), by
\[
 \mathcal C_P=\frac1h\sum_{\iota=E,F,K}[P,X_\iota]A_\iota.
 \tag{4}
\]
Then the exact finite identity is
\[
 \boxed{\quad
 \mathcal C_P=
 \frac{\epsilon\eta}{h}(Q^{-1}T_0-T_1)\otimes g_B
 +\frac{(Q^{-1}-1)x^{-1}\epsilon}{h}
                         E_{01}\otimes F_Bg_B .
 \quad}
 \tag{5}
\]
Here \(T_a=e_ae_a^*\) and \(E_{01}=e_0e_1^*\).
All matrices retain the actual zero arrows at both ends.

Indeed \([T_0,E_1]=\epsilon E_{01}\),
\([T_0,F_1]=-\eta E_{10}\), and
\(g_BE_B=QE_Bg_B,\ g_BF_B=Q^{-1}F_Bg_B\).
In \([P,E_*]A_E\), the cut term is
\(\epsilon\eta Q^{-1}T_0\otimes g_B\). Its tail term contains
\(T_0F_1=0\) and vanishes. In \([P,F_*]A_F\), the cut term is
\(-\epsilon\eta T_1\otimes g_B\); the remaining term is
\((Q^{-1}-1)x^{-1}\epsilon E_{01}\otimes F_Bg_B\).
This proves (5), including all tail-pivot terms.

There is a version without division by either edge coefficient:
\[
 \boxed{\quad
 h\mathcal C_P=
   (\epsilon\eta Q^{-1}T_0-F_1T_0E_1)\otimes g_B
 +(Q^{-1}-1)x^{-1}T_0E_1\otimes F_Bg_B .
 \quad}
 \tag{6}
\]
It follows from \(F_1T_0E_1=\epsilon\eta T_1\) and
\(T_0E_1=\epsilon E_{01}\). These are whole matrix identities,
including at zeros of \(\epsilon\).

For every finite inserted matrix \(B\) and whole marked word \(O\),
[W]'s sourced identity now reads
\[
 \Phi_O(\mathcal D_N B)
 =\varkappa_\beta\operatorname{Tr}(\mathcal C_PBO)
 +\frac{\varkappa_\beta}{h}\sum_\iota
                 \operatorname{Tr}(PA_\iota B[O,X_\iota]).
 \tag{7}
\]
The second term is retained in its actual word order. It vanishes
for the unmarked intertwining word; clocks need not commute with
these generators. The local construction below realizes the first
term for \(B=I\), with arbitrary retained stage clocks. It is not
an automatic coarea construction for an arbitrary growing matrix \(B\).

At \(M=1\), \(\eta=Q\epsilon\), so
\[
 \mathcal C_P=\frac{\epsilon^2}{h}
 \bigl[(T_0-QT_1)\otimes g_B+x^{-1}E_{01}\otimes F_Bg_B\bigr].
 \tag{8}
\]
Declare the displayed factorial basis orthonormal. At completeness,
\(\|E\|,\|F\|\le2\), while \(K,g\) are unitary. The coproduct
therefore gives \(\|F_B\|\le2(b-1)\). Since
\(|\epsilon|=|e^{-h}-1|\le|h|\) on this imaginary root value,
\[
 \|\mathcal C_P\|\le(2b-1)|h|,\qquad
 \frac{\|\mathcal C_P\|_{\rm HS}}{\|P\|_{\rm HS}}
       \le\sqrt2(2b-1)|h|,\qquad
 \|P\|_{\rm HS}=N^{(b-1)/2}.
 \tag{9}
\]
The rank bound uses only the two cut output rows. This is an
actual value-level almost-invariance estimate for the unmarked
adjoint boundary. It neither controls marked internal defects nor
makes all meridian normals small: \(\partial_M\epsilon\) is of
order one and the full scalar framing also has to be differentiated.

## 2. Exact polynomial coupons and their cut matrix

Let \(F_a=(Q;Q)_a\), \(0\le a<N\), and write the factorial vector as
\(w_a=v_a/F_a\). Every \(F_a\) is nonzero at this root. In the
polynomial basis \(v_a=Z^a\), conjugation gives
\[
 F_vv_a=v_{a+1},\qquad
 E_vv_a=(1-Q^a)(MQ^{-a}-M^{-1})v_{a-1},\qquad
 K_vv_a=xQ^{-a}v_a,
 \tag{10}
\]
with the actual finite upper and lower arrows truncated. Consequently
\[
 T_0E_v=\eta\epsilon\,T_0\partial_1,\qquad
 F_vT_0E_v=\eta\epsilon\,Z_1T_0\partial_1
                         =\eta\epsilon T_1.
 \tag{11}
\]
No factorial with index \(N\) has been divided out.

Distinguish the \(b\)-by-\(b\) deletion matrix
\(T_{\rm del}=\operatorname{diag}(0,1,\ldots,1)\) from its
second quantization \(\Pi_0=\Gamma(T_{\rm del})\).
On the full polynomial ring put
\[
 T(\sigma,\mathbf t)
  =T_{\rm del}+\sigma E_{11}+\sum_{i=2}^b t_iE_{i1}.
 \tag{12}
\]
Then, at \(\sigma=\mathbf t=0\),
\[
 \Gamma(T)=\Pi_0,\qquad
 \partial_\sigma\Gamma(T)=\Pi_1,\qquad
 \partial_{t_i}\Gamma(T)=Z_i\Pi_0\partial_1 .
 \tag{13}
\]
To prove this, apply the substitution to
\(Z_1^aZ_2^{a_2}\cdots Z_b^{a_b}\): its first factor becomes
\((\sigma Z_1+\sum t_iZ_i)^a\). Each first derivative at zero
selects exactly \(a=1\), with coefficient one.
Thus the diagonal grading is \(\sigma^a\), not the head matrix
\(\operatorname{diag}(\sigma,1,\ldots,1)\).
For a finite \(N\)-head tensor space, sandwich these polynomial
operators between its inclusion and projection. This preserves
(13) with every actual top truncation.

The remaining tail raising matrix is
\[
 F_{B,v}=\sum_{i=2}^b
       x^{-(i-2)}\Gamma(D_i(h))Z_i,\qquad
 D_i(h)=\operatorname{diag}
       (1,\underbrace{Q,\ldots,Q}_{2,\ldots,i-1},1,\ldots,1).
 \tag{14}
\]
This is the literal iterated coproduct, not an averaged tail.
In particular \(D_i\) acts trivially on variables \(1,i\).
Its second quantization is a finite shift of the retained endpoint
clocks. No clock is discarded or Taylor-truncated.

## 3. A sourced parameter family with the correct pivots

For the ordinary analytic family use
\[
 Q=e^h,\quad q=e^{h/2},\quad x=q^{-1}\sqrt Y,\quad M=-\sqrt Y,
 \quad G_h=\operatorname{diag}(1,Q^{-1},\ldots,Q^{-1}).
 \tag{15}
\]
Keep the chosen square-root sheet. Let \(O_m\) be the literal
crossing word of [F] with all its fixed stage clocks. Define, first
degree by degree with a total-index grading \(\tau\),
\[
 \mathscr Z_i(h,Y,m;\sigma,\mathbf t;\tau)
 =x^c\operatorname{Tr}_{\rm Sym}
  \bigl[\Gamma(\tau I)\,
        O_m\,\Gamma(D_i(h))\Gamma(T(\sigma,\mathbf t))
                                  \Gamma(G_h)\bigr].
 \tag{16}
\]
Here \(c=b-1-\operatorname{wr}(\beta)\);
write \(\mathscr Z_0\) for \(D_0=I\).
The pivot \(Q^{-a}\) appears only on the closed tail heads.
There is no new cut pivot. The order in (16) is part of the source.
Finite-degree cyclicity, (11)--(14), give the ordinary boundary
family at grading one:
\[
 \boxed{\quad
 \mathscr B_{\rm ord}=
 \frac{\eta\epsilon}{h}
 \left[
 Q^{-1}\mathscr Z_0|_0-\partial_\sigma\mathscr Z_0|_0
 +(Q^{-1}-1)x^{-1}
       \sum_{i=2}^b x^{-(i-2)}\partial_{t_i}\mathscr Z_i|_0
 \right].
 \quad}
 \tag{17}
\]
The notation \(|_0\) means zero cut parameters; it does not set
the original clocks to zero. In (17),
\(\eta=1-e^h\) and \(\epsilon=Me^{-h}-M^{-1}\).
Thus \(\eta\epsilon/h\) is analytic at \(h=0\).
The construction uses the entire coefficient, not \(1/\epsilon\).

For the literal finite-root contraction the same formula holds
with each trace replaced by its finite-head trace and with the
whole external multiplier
\[
                              x^{-Nc}.
 \tag{18}
\]
Indeed the ordinary external line is \(x^c\), whereas the root line
is \(x^{-c(N-1)}\), as recorded in [R]. All index-dependent root
pivots are \(Q^{-a}\) and are already in \(G_h\).
Formula (18) is retained before all meridian differentiation.
At the complete root its value is one because \(c\) is even;
its derivatives are not thereby one or zero.

## 4. Joint completion and the moving determinant zero

Here is the analytic justification for using cut parameters in
the ordinary source, without postulating a new scalar summation.
Every operator in (16) preserves total polynomial degree.
At degree \(T\), the crossing sum is finite and
\(\Gamma(T(\sigma,\mathbf t))\) has norm at most \(C^T\) on each
fixed compact parameter set. The diagonal factors in (15)--(16)
have the same property. This changes only exponential constants
in the original finite-sector estimates.

At order \(h^j\), [F]'s exact differential-operator calculation
still gives a finite sum of \(D\Gamma(L_\beta)\) with
\(\operatorname{ord}D\le2j\), including the actual pivots and clocks.
Nothing is moved through the possibly singular cut matrix.
The remaining classical matrix is instead
\[
 B_\lambda(Y)=L_\beta(\sqrt Y)T(\sigma,\mathbf t),\quad
 D_\lambda(Y)=\det(I-B_\lambda(Y)),\qquad
 \lambda=(\sigma,\mathbf t).
 \tag{19}
\]
Matrix-directional differentiation of the determinant inverse
proves rational grading continuation, with denominator at most
\(\det(I-\tau B_\lambda)^{2j+1}\) and numerator grading degree
bounded linearly in \(j\). This argument does not invert
\(T(\sigma,\mathbf t)\). At fixed order, derivatives in the cut
parameters commute with that rational continuation.

Suppose \(\alpha\ne0,1\) is a simple zero of the original
\(\Delta_K\). At \(\lambda=0\),
\(D_0(Y)=Y^{c/2}\Delta_K(Y)\). The analytic implicit equation
therefore gives a unique nearby simple root \(\alpha(\lambda)\).
Put \(z_\lambda=Y-\alpha(\lambda)\). The rank-one residue
factorization and hard remainder are jointly analytic:
\[
 B_\lambda(I-B_\lambda)^{-1}
       =u_\lambda v_\lambda^T/z_\lambda+G_\lambda(Y),\qquad
 r_\lambda(Y)=Y^{c/2}z_\lambda/D_\lambda(Y).
 \tag{20}
\]
One nonzero adjugate entry gives this local factorization.
No assumption \(v_\lambda^Tu_\lambda\ne0\), and no inverse of a
cut projector, is needed.

The finite normal products and literal Poisson blocks in [G]
are unchanged. Only the analytic matrix entries in (20) change.
Its hard embedding uses \(G_\lambda\), never \(G_\lambda^{-1}\).
The unit hard Hessians, the small stationary branches, and the
analytic raw-amplitude bounds consequently persist on common
smaller parameter disks. Explicitly the scalar defect estimates
are unchanged, the finitely many linear substitutions have bounded
coefficients, and the finite implicit inverses have a common
nonzero Jacobian. The composition estimate
\(\prod j_\nu!\le(\sum j_\nu)!\) gives
\[
                 \|\mathcal A_{\lambda,j}\|\le MC^j j!
 \tag{21}
\]
uniformly on these disks and fixed clock compacts.
This verifies the parametric use of [G]'s construction from its
literal operations; it is not an inference from scalarity at a root.
The additional \(D_i(h)\) factors are analytic near the identity
and are retained among the amplitude factors.

The soft endpoint stays \(x_{\rm s}=0\). In particular the
parameter-dependent phase has
\(f_\lambda(Y,x_{\rm s})=z_\lambda x_{\rm s}+O(x_{\rm s}^2)\).
At a fixed \(Y_0\ne\alpha\) sufficiently near \(\alpha\), shrink
the cut-parameter disk so \(Y_0\ne\alpha(\lambda)\).
The inverse soft coordinate, compact relative chains and ordinary
Borel germs are then jointly holomorphic on a common local domain.

## 5. Differentiating the whole finite coarea current

Use the common Gaussian dimension \(2d\) from [G], put \(p=d+1\),
and retain its normalized volume \(\Omega_\lambda\). For each
family (16), its original Borel germ has the exact form
\[
 b_{i,\lambda}=r_\lambda\,\partial_\xi^p J_{i,\lambda},\qquad
 J_{i,\lambda}(Y,\xi)=
 \int_{\mathcal D_{\lambda,\xi}(Y)}
 \widehat{\mathcal A}_{i,\lambda}
       (\xi-\mathcal F_\lambda,Y,x_{\rm s},X,m)\,\Omega_\lambda,
 \qquad J_{i,\lambda}=O(\xi^p).
 \tag{22}
\]
All cut derivatives in (17) act on this entire holomorphic period:
on its residue, phase, coordinate maps, density, amplitude, and
chain. In particular \(\alpha(\lambda)\) is differentiated.
Freezing the old root or the old chain would give a different source.

Choose a common sufficiently short \(R\ne0\), and set
\[
 U_{i,\lambda,R}=\frac1h\int_0^R e^{-\xi/h}b_{i,\lambda}(Y,\xi)d\xi,
 \qquad
 E_{i,\lambda,R}=
       \sum_{k=0}^{p-1}h^{-k-1}
                     \partial_\xi^{p-1-k}J_{i,\lambda}(Y,R).
 \tag{23}
\]
The exact identity [C] is uniform in these parameters:
\[
 U_{i,\lambda,R}
 =r_\lambda h^{-p}
   \int_{\mathcal D_{\lambda,R}}
      e^{-\mathcal F_\lambda/h}
      \mathcal A_{i,\lambda,\mathrm{fin}}
                   (h,R-\mathcal F_\lambda)\,\Omega_\lambda
       +r_\lambda e^{-R/h}E_{i,\lambda,R},
 \tag{24}
\]
where the finite raw-amplitude integral still starts at zero.
The common compact coordinates of [C] justify differentiation
of (22)--(24). Every lower jet below order \(p\) vanishes because
\(J_{i,\lambda}=O(\xi^p)\) holds jointly; every upper jet in (23)
is retained and differentiated. Thus the derivatives selected by
(13), with the finite clock shifts (14), are actual local sourced
coarea currents, rather than only principal symbols of coupons.

Analytic scalar factors in (17)--(18) must also be treated at the
level of the whole Borel source. If
\(a(h)=a_0+\sum_{n\ge1}a_nh^n\), let
\(g_a(\xi)=\sum_{n\ge1}a_n\xi^{n-1}/(n-1)!\). Exactly
\[
                \mathcal B_0(a\mathscr Z)
                         =a_0 b+g_a*b .
 \tag{25}
\]
This converges on the common local Borel disk and retains the
base-zero primitive. One may equivalently put \(a(h)\) in the
raw amplitude before constructing (22)--(24).
Multiplying just the finite cutoff \(U_R\) by \(a(h)\) need not
equal the cutoff of (25); its endpoint terms must not be lost.
For each fixed \(N\), the whole \(x^{-Nc}\) can be included this
way on the chosen sheet. No uniform-in-\(N\) bound is asserted
for its derivatives or for that analytic extension.

## 6. The exact scope of the source correspondence

The ordinary-color restriction is literal. At \(x=q^{L-1}\),
\(L\ge2\), the color-block zeros in [F] prevent a high occupation
from dropping below \(L\) along a physical strand. The coupons
in (13) restrict the cut occupation to zero or one; their tail
arrows only raise an occupation. Thus a high occupation in a
surviving closed path would propagate to a cut occupation below
\(L\), impossible. All intermediate occupations are below \(L\).
The differentiated families in (17), with their full clocks,
therefore agree coefficientwise with the corresponding ordinary
finite-color coupon contractions. As in [F], rational grading
completion at \(Y=1\) is legitimate; the undeformed classical
deleted permutation is nilpotent there. Only the indicated
finite parameter derivatives are claimed to have this restriction,
not the entire nonzero-\(\sigma\) family.

Separately, (5)--(7), (10)--(14), and the finite-trace version of
(17)--(18) are exact for every fixed root level and the whole
meridian variable. Their proof used finite matrices only.
The ordinary analytic Borel construction is not an equality of
that untruncated completion with the whole fixed-\(N\) meridian
germ, nor a choice of its physical summation. In particular all
fixed-level meridian normals and the original scalar line remain
necessary data in any further comparison.

This establishes a local source-preserving coupon/current map
with the actual cut, tail pivots, full clocks and finite endpoints.
The internal marked commutator in (7) remains a separate explicit
source. A global geometric boundary transport, the regular
primitive filling factor, and a nonzero original closing
coefficient are not consequences of this local adapter.

## 7. Complete proof directs

| Label | Complete source | SHA256 |
|---|---|---|
| W | notes/research_actual_weighted_ward_centralizer_lift.md | e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a |
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| R | notes/research_actual_finite_transfer_poisson_wall.md | 502dda2160119c34959965e1c4c71d2a77864325d48fd6df0853a9260a60a2ed |
| G | notes/research_actual_source_finite_gaussian_borel_period.md | dda9ec95e7fc460dc965cc70c21d94e6d7e412bcdc4521b42c4137da3e00c9c8 |
| C | notes/research_finite_gaussian_cutoff_boundary_currents.md | f7ab590bb206b012ce9c462db452e2d9526f1dfedad679924aa55ebe160a7c6c |

W supplies the actual finite Ward matrices and sourced identity;
F the literal ordinary source and differential trace completion;
R the retained root/ordinary framing ratio; G the finite raw
Wick/coarea construction; C its complete finite endpoint adapter.
All complete directs were read and all used implications checked.
The cofactor, second-quantized parameter derivatives and parametric
source/current calculation are proved here. Only written mathematics,
source-text operations and hash checks were used. Frozen notes and
public manuscripts are unchanged.
