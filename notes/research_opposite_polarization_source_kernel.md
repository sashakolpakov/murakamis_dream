# Opposite-polarization kernels and the original closing source

Private written proof, 18 November 2026.

The actual total lowering power, balanced turnover, and prefix quotient
give a finite operator between the two polarizations. Its normalization
is exactly the inverse-Jacobian coupon of the original pointed source.
Two normalized kernels sew to that source, on the original compact
coherent cycles. Their root Laurent coefficients recover the first
meridian jet and give an explicit contracting homotopy on every
nonself reciprocal physical-weight pair.

This is also a relative-source construction: restricting a resolution
to a subchain produces a specified operator defect and its boundary
transgression. Neither the defect nor the complementary chains are
discarded. No geometric contribution is selected by generic
invertibility or by the contracting homotopy.

The complete directs R, P, and Z are pinned below. They supply the
actual quotient, balanced turnover, and original source normalization.
The power product, normalized sewing, Laurent algebra, and relative
kernel statements are proved here.

## 1. The literal map and its balanced scalar

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(m\ge2\) heads at the common meridian \(M\) near one. The quantum
parameter is fixed. Put \(r=m-1\), \(x=-M/q\), and
\[
 K_{\rm r}(M)=M^rK_0,\qquad
 K_0^N=\varepsilon I,\qquad
 \varepsilon=(-1)^{(N+1)r}.
 \tag{1}
\]
The remaining occupation space is a fixed vector space \(U\).
All reflected maps below use its same ordered basis.

Use the actual ordered total matrices \(E_\Sigma,F_\Sigma,K_\Sigma\),
where \(E\) is the scaled balanced lowering operator. On one head,
\[
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad
 Ew_a=(MQ^{-a}-M^{-1})w_{a-1},\qquad Kw_a=xQ^{-a}w_a.
 \tag{2}
\]
The missing extreme arrows are zero. In particular \(E^N=F^N=0\).
The same identities hold for the totals: the two terms in
\(E_1K_{\rm r}+E_{\rm r}\) \(Q\)-commute, and those in
\(F_1+K_1^{-1}F_{\rm r}\) \(Q^{-1}\)-commute. The finite binomial
formula at a primitive \(N\)-th root has zero intermediate
coefficients in degree \(N\). Induction over the heads proves
\[
 E_\Sigma^N=F_\Sigma^N=0.
 \tag{3}
\]

R's actual triangular matrix and quotient maps are
\[
 S(M)=\sum_{j=0}^{d}
 \frac{(x^{-1}L_1F_{\rm r})^j}{\prod_{a=1}^j(1-Q^a)},\qquad
 q_F(M)=p_0S(M)^{-1},\qquad i_F(M)=S(M)i_0=i_0.
 \tag{4}
\]
They are holomorphic near one, \(q_Fi_F=I\), and
\(\ker q_F=F_\Sigma V\). For a total intertwiner \(W\),
\[
 B(W)=q_FW i_F,\qquad q_FW=B(W)q_F.
 \tag{5}
\]
The second identity follows either from the quotient or directly
from R's expansion \(S^{-1}WS=\sum F_1^nB_n\).

Retain the entire balanced turnover
\[
 C(M)w_a=c_a(M)w_{d-a},\qquad
 c_a(M)=\prod_{j=1}^a\frac{MQ^j-M^{-1}}{1-Q^j},\qquad
 \mathscr C(M)=C(M)^{\otimes m}\mathsf J,
 \tag{6}
\]
where \(\mathsf J\) reverses the factors. P proves, with the original
Cartan and crossing scalars,
\[
 \mathscr C F_\Sigma(M^{-1})=E_\Sigma(M)\mathscr C,\quad
 \mathscr C E_\Sigma(M^{-1})=F_\Sigma(M)\mathscr C,\quad
 K_\Sigma(M)\mathscr C=\mathscr C K_\Sigma(M^{-1})^{-1}.
 \tag{7}
\]
There is a scalar which must not be suppressed:
\[
 \mathscr C(M)\mathscr C(M^{-1})=\gamma_N(M)^mI,\qquad
 \gamma_N(M)=(-1)^d\frac{D_N(M)}{N},\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{8}
\]
Indeed \(c_{d-a}(M)c_a(M^{-1})\) is independent of \(a\).
Its consecutive ratio is one after replacing \(Q^{d-a}\) by
\(Q^{-a-1}\). At \(a=0\), the root product
\(\prod_{j=1}^d(1-Q^j)=N\) gives \(c_d(M)=\gamma_N(M)\).
The Laurent-polynomial continuation defines \(D_N\) at \(z=\pm1\).

Define the actual analytic matrix
\[
 \boxed{\quad
 T(M)=q_F(M)E_\Sigma(M)^d\mathscr C(M)i_F(M^{-1}).
 \quad}
 \tag{9}
\]
Equivalently the rightmost factor is \(S(M^{-1})i_0\).
It descends from the reflected quotient: adding
\(F_\Sigma(M^{-1})v\) to a representative gives zero after
\(E_\Sigma^d\mathscr C\), by (3),(7). More explicitly it factors as
\[
 V(M^{-1})/F_\Sigma V(M^{-1})
 \ \xrightarrow{\ \mathscr C\ }\ V(M)/E_\Sigma V(M)
 \ \xrightarrow{\ E_\Sigma^d\ }\ker E_\Sigma(M)
 \ \xrightarrow{\ q_F\ }\ V(M)/F_\Sigma V(M).
 \tag{10}
\]
Every arrow here is an actual finite linear map.

Let \(\beta^{\rm rev}\) replace \(\sigma_i^{\pm1}\) by
\(\sigma_{m-i}^{\pm1}\), without reversing word order. Write
\(B_+(M)=B(W_\beta(M))\) and \(B_-(M)=B(W_{\beta^{\rm rev}}(M))\).
P's whole-meridian turnover and (5),(7) imply
\[
 B_+(M)T(M)=T(M)B_-(M^{-1}),\qquad
 K_0T(M)=T(M)K_0^{-1}.
 \tag{11}
\]
For the first identity, the difference between
\(W_{\beta^{\rm rev}}i_F\) and \(i_FB_-\) lies in \(F_\Sigma V\)
and is killed in (9). For the second use
\(K_\Sigma E_\Sigma^d=Q^{-1}E_\Sigma^dK_\Sigma\),
the quotient and section rows
\(q_FK_\Sigma=xK_{\rm r}q_F\),
\(K_\Sigma i_F=i_FxK_{\rm r}\), and
\(x(M)x(M^{-1})=Q^{-1}\). The scalar first-head Cartan
substitution is made only in these rows.

The prescribed zero-framing line is reciprocal and stays in \(W\),
as in P. Any additional external scalar remains explicit. Marks
not satisfying the indicated intertwining and turnover retain
their defect; (11) is not imposed on them.

## 2. Exact double composition and source normalization

Put
\[
 H(M)=D_N(MK_{\rm r}(M)),\qquad
 a_N(M)=(-1)^dN\,\gamma_N(M)^m .
 \tag{12}
\]
Then
\[
 \boxed{\quad T(M)T(M^{-1})=a_N(M)H(M).\quad}
 \tag{13}
\]
Here is a proof including the lowering product. With
\(\Omega_\Sigma=F_\Sigma E_\Sigma+qK_\Sigma+
q^{-1}K_\Sigma^{-1}\), set
\(v(k,\omega)=\omega-qk-q^{-1}k^{-1}\).
The commutation relations give by induction
\[
 E_\Sigma^dF_\Sigma^d
       =\prod_{j=1}^{d}v(Q^{-j}K_\Sigma,\Omega_\Sigma).
 \tag{14}
\]
Both \(K_\Sigma\) and \(\Omega_\Sigma\) descend to the \(F\) quotient.
There their values are
\[
 K_\Sigma=-z/q,\qquad \Omega_\Sigma=-z-z^{-1},
                    \qquad z=MK_{\rm r}.
\]
Thus each factor in (14) becomes
\((1-Q^j)(zQ^{-j}-z^{-1})\). The two finite products give
\[
 q_FE_\Sigma^dF_\Sigma^di_F=(-1)^dN D_N(MK_{\rm r}).
 \tag{15}
\]
In composing (9), replace \(i_F(M^{-1})q_F(M^{-1})\) by \(I\):
its difference has image in \(F_\Sigma(M^{-1})V\), which the
left factor \(E_\Sigma^d\mathscr C\) annihilates. Equations
(7),(8),(15) then give (13). The reflected identity follows too.

From (11) and \(D_N(z^{-1})=D_N(z)\),
\[
 H(M)T(M)=T(M)H(M^{-1}).
 \tag{16}
\]
On a sufficiently small punctured meridian disk all these \(H\)'s
are invertible. Set
\[
 \boxed{\quad J(M)=H(M)^{-1}T(M).\quad}
 \tag{17}
\]
This is precisely source normalization, rather than an arbitrary
normalizing scalar. Z's central coupon
\(Z_N=U_{N-1}(-\Omega_\Sigma)^{-1}\) has
\(q_FZ_N=H^{-1}q_F\): the first block row of its actual triangular
matrix inverse proves this equality. Hence
\[
 J(M)=q_F(M)Z_N(M)E_\Sigma(M)^d\mathscr C(M)i_F(M^{-1}).
 \tag{18}
\]
Its exact reflection law and generic inverse are
\[
 J(M)J(M^{-1})=a_N(M)H(M)^{-1},\qquad
 J(M)^{-1}=a_N(M)^{-1}T(M^{-1}).
 \tag{19}
\]
In particular the failure of a reflection square to be \(I\)
is the specified central source kernel.

The poles of \(J\) at completeness have order at most one.
On \(K_0=\chi\), put \(z=M^m\chi\). Then
\[
 H(M)^{-1}\big|_\chi
 =\frac{M^m\chi-M^{-m}\chi^{-1}}
        {\varepsilon(M^{mN}-M^{-mN})}.
 \tag{20}
\]
For \(\chi\ne\chi^{-1}\) the denominator has a simple zero;
for \(\chi=\pm1\) the quotient is removable. Since \(T\) is
analytic, this proves the assertion without a bound on its
norm. All these statements concern fixed-root meridian normals,
not ordinary quantum-parameter normals.

## 3. Two kernels sew to the original pointed functional

The exact original highest-cut and pivotal source is
\[
 \Phi_0(W)=\operatorname{Tr}_{V}
             ((P_0\otimes K_{\rm r}^{1-N})W)
          =D_N(M)\operatorname{Tr}_{U}(H(M)^{-1}B_+(M)),
 \tag{21}
\]
by R and Z. Equations (11),(16),(19) give the stronger matrix identity
\[
 J(M)B_-(M^{-1})J(M^{-1})
             =a_N(M)H(M)^{-1}B_+(M).
 \tag{22}
\]
Consequently
\[
 \boxed{\displaystyle
 \Phi_0(W_\beta(M))=
 \frac{D_N(M)}{a_N(M)}
 \operatorname{Tr}_{U}\!
       \left(J(M)B_-(M^{-1})J(M^{-1})\right).
 }\tag{23}
\]
All meromorphic expressions have the continuation prescribed by
the original analytic left side. Even though the individual
\(J\)'s can have simple poles, the sewn matrix in (22) has at
most a simple pole. Its residue has zero trace. This cancellation
uses exact composition; it is not a pointwise cancellation of
an unintegrated product of coherent kernels.

For arbitrary reduced matrices \(A_+,A_-\), the corresponding
defect is explicit. Put \(\Delta=A_+T-TA_-\). Direct multiplication
gives
\[
 J A_- J(M^{-1})
       =a_NH^{-1}A_+-H^{-1}\Delta J(M^{-1}).
 \tag{24}
\]
Thus neither inserted marks nor localized windows are made
intertwiners by the normalization. Formula (24) is a matrix
identity, independent of any source formula for a nonintertwining
mark.

## 4. Root Laurent algebra and the first meridian jet

Use \(u=\Log M\) and define
\[
 \sigma=(-1)^{d(m+1)},\qquad
 J(e^u)=\frac{R}{u}+J_0+uJ_1+O(u^2).
 \tag{25}
\]
Here \(R\) is the residue matrix, not a crossing.
The scalar \(a_N(e^u)\) is even and \(a_N(1)=\sigma N\).
Expansion of (20) gives
\[
 H(e^u)^{-1}
 =\frac{K_0-K_0^{-1}}{2\varepsilon mN\,u}
   +\frac{K_0+K_0^{-1}}{2\varepsilon N}+O(u).
\]
Comparing the three first coefficients in (19) proves
\[
 \boxed{\begin{split}
 R^2&=0,\\
 [R,J_0]&=\frac{\sigma}{2\varepsilon m}(K_0-K_0^{-1})=:D,\\
 J_0^2-RJ_1-J_1R&=\frac{\sigma}{2\varepsilon}(K_0+K_0^{-1}).
 \end{split}}\tag{26}
\]
These are identities of the actual finite matrices.

All coefficients of \(J\) reverse the \(K_0\) weights, by (11).
On any nonself pair \(U_\chi\oplus U_{\chi^{-1}}\), \(D\) is
invertible and \(DR=-RD\). Thus
\[
 h=J_0D^{-1},\qquad Rh+hR=I
 \tag{27}
\]
on this pair. This is an explicit contracting homotopy for
the square-zero residue. In particular \(\ker R=\operatorname{im}R\)
there and its rank is half the pair dimension. On self weights
\(R=0\), and the constant identity in (26) instead makes \(J_0\)
invertible. No norm bound for this homotopy is asserted.
In particular the differences \(\chi-\chi^{-1}\) can approach
zero as \(N\) varies.

Nor is (27) an unqualified equivariant contraction. If
\(B_\pm(e^u)=B_{\pm,0}+uB_{\pm,1}+O(u^2)\), the actual
intertwining equation \(J(e^u)B_-(e^{-u})=B_+(e^u)J(e^u)\)
gives exactly
\[
 RB_{-,0}=B_{+,0}R,\qquad
 J_0B_{-,0}-B_{+,0}J_0=B_{+,1}R+RB_{-,1}.
 \tag{27a}
\]
Its finite part therefore retains the first normal rows.

The contraction does not make the source zero. To see exactly
what remains, write
\[
 B_-(e^u)=B_0+uB_1+\tfrac12u^2B_2+O(u^3).
\]
Also
\[
 \frac{D_N(e^u)}{a_N(e^u)}
       =\sigma\left(\frac{N}{D_N(e^u)}\right)^{m-1}
       =\sigma+O(u^2).
 \tag{28}
\]
The product in (22) has no coefficient of \(u^{-2}\).
Its finite trace, calculated before suppressing any normals, is
\[
 \operatorname{Tr}\left[
 B_0(J_0^2-RJ_1-J_1R)+B_1[R,J_0]\right].
 \tag{29}
\]
Indeed the apparent second-derivative term is
\(-\tfrac12\operatorname{Tr}(RB_2R)
=-\tfrac12\operatorname{Tr}(R^2B_2)=0\).
The other terms follow by multiplying (25); cyclicity gives
the displayed orders. Inserting (26) into (23),(28),(29) yields
\[
 \boxed{\displaystyle
 \Phi_0(W_\beta(1))=
 \frac1{2\varepsilon}\operatorname{Tr}((K_0+K_0^{-1})B_0)
 +\frac1{2\varepsilon m}\operatorname{Tr}((K_0-K_0^{-1})B_1).
 }\tag{30}
\]
This is the original first-jet closing row, now assembled from
the two opposite-polarization kernels. Here \(B_0,B_1\) initially
belong to the reversed word. The actual half-twist conjugates
it to the original word and its reduced matrix commutes with
\(K_0\); cyclic trace, including its differentiated commutator,
therefore gives the same row for \(B_+\).

Equation (29) uses the full trace. On relative windows, neither
\(R^2=0\) with intervening windows nor the trace cancellation
of the \(B_2\) term can be assumed. Those terms stay in the
unassembled meromorphic kernel.

### Exact integer-degree pairs

The actual map (9) has a stronger grading property than its
Cartan-weight reversal. Let \(U_k\) be the remaining occupation
space with total integer degree \(k\), \(0\le k\le rd\).
The map \(i_F\) inserts first occupation zero, \(\mathscr C\)
changes total degree \(k\) to \(md-k\), and \(E_\Sigma^d\)
lowers it by \(d\). Every term of \(S\) and \(S^{-1}\)
preserves total degree, and \(p_0\) extracts degree zero in
the first head. Therefore, exactly,
\[
 T(M)U_k\subset U_{rd-k},\qquad J(M)U_k\subset U_{rd-k}.
 \tag{30a}
\]
The diagonal normalization in (17) does not change this rule.
Generic invertibility in (13),(19) makes each indicated block
an isomorphism, with the reflected block as its inverse up to
the specified diagonal scalar.

For an actual braid word, \(B_\beta\) preserves the integer
degree: each original crossing preserves the sum of its
occupations, and the quotient (4) preserves degree too.
Define its exact finite sector trace by
\[
 t_k^\beta(M)=\operatorname{Tr}_{U_k}B_\beta(M).
\]
Equation (11), applied to the isomorphisms (30a), gives
\(t_k^\beta(M)=t_{rd-k}^{\beta^{\rm rev}}(M^{-1})\)
generically. The reduced half twist is also an actual
degree-preserving invertible braid operator, so it removes
the word reversal within each integer sector. Holomorphic
continuation then proves the whole-meridian identities
\[
 \boxed{\quad
 t_k^\beta(M)=t_{rd-k}^\beta(M^{-1}),\qquad
 \mathcal F_\beta(v,M)
      =v^{rd}\mathcal F_\beta(v^{-1},M^{-1}),\quad
 \mathcal F_\beta(v,M)=\sum_{k=0}^{rd}v^k t_k^\beta(M).
 \quad}\tag{30b}
\]
The last equality is a finite polynomial identity, continued
at \(v=0\); it does not interpolate the integer index \(k\).
At \(M=1\) the sector values agree and their first meridian
derivatives are opposite. For a self sector \(k=rd/2\), the
first derivative vanishes.

This also refines the scalar closing bookkeeping to integer
degree pairs. Put \(\chi_k=x_0^rQ^{-k}\), \(x_0=-q^{-1}\).
Since \(d=N-1\), \(\chi_{rd-k}=\chi_k^{-1}\). Formula (21)
is exactly the sum of the meromorphic scalar terms
\[
 \phi_k(M)=
 \frac{D_N(M)(M^m\chi_k-M^{-m}\chi_k^{-1})}
 {\varepsilon(M^{mN}-M^{-mN})}\,t_k^\beta(M).
 \tag{30c}
\]
For \(k\ne rd-k\), (30b) cancels the possible residue of
\(\phi_k+\phi_{rd-k}\) within this pair. Expansion at one gives
\[
 \boxed{\quad
 (\phi_k+\phi_{rd-k})(1)=
 \frac{\chi_k+\chi_k^{-1}}{\varepsilon}t_k^\beta(1)
 +\frac{\chi_k-\chi_k^{-1}}{\varepsilon m}
                         (t_k^\beta)'(1).
 \quad}\tag{30d}
\]
This remains valid if the two distinct integer sectors happen
to have self-reciprocal Cartan weight. A self integer sector
has \(\chi_k^2=1\), is counted once, and contributes
\(\chi_k t_k^\beta(1)/\varepsilon\).

These are removable scalar contributions of the actual reduced
trace and its capped integer sectors. An individual \(U_k\)
projector has not been lifted to an analytic original
total-intertwiner projector through the root: the Casimir
localizers in P distinguish only the Cartan weights modulo
\(N\), and retain their collisions. No such lift, geometric
Morse projector, angular cycle coefficient, or complex-index
continuation follows from the finite graded reciprocity.
The relative-window defects below remain.

## 5. Exact compact coherent convolution

This section uses the original binomial head metric, without a
new Fourier or Gaussian gauge. Let
\[
 X=(\mathbb P^1\times\mathbb P^1)\setminus\{1+wz=0\},\quad
 \Gamma=\{w=v,\ z=\bar v\},\quad
 \nu=-\frac{dw\wedge dz}{2\pi i(1+wz)^2}.
\]
For a head set
\[
 c(z)_a=\binom da z^a,\qquad v(w)_a=w^a,\qquad
 \Pi(w,z)=\frac{c(z)v(w)}{(1+wz)^d}.
 \tag{31}
\]
This is the same coherent projector as Z. It is a global
matrix-valued function on \(X\). On \(r\) heads use tensor
products and write \(\nu^{[r]}\) for the ordered product.
The elementary beta moments give
\[
 N^r\int_{\Gamma^r}\Pi\,\nu^{[r]}=I,\qquad
 K_A(\mathbf w,\mathbf z)=v(\mathbf w)A c(\mathbf z).
 \tag{32}
\]
For one head the moment is
\(\int_\Gamma w^a\binom db z^b(1+wz)^{-d}\nu
=\delta_{ab}/N\); tensor multiplication proves (32).
The identity kernel is exactly \(\prod_i(1+w_i z_i)^d\).
Every head occupation remains \(0,\ldots,d\).

For three copies \(x_l=(\mathbf w_l,\mathbf z_l)\) of \(X^r\),
with \(l=0,1,2\), put
\[
 \mathcal K(M;x_0,x_1,x_2)=
 \frac{D_N(M)}{a_N(M)}
 K_{J(M)}(\mathbf w_0,\mathbf z_1)
 K_{B_-(M^{-1})}(\mathbf w_1,\mathbf z_2)
 K_{J(M^{-1})}(\mathbf w_2,\mathbf z_0)
 \prod_{l=0}^2\prod_{i=1}^r
 \left[-\frac{dw_{l,i}\wedge dz_{l,i}}
 {2\pi i(1+w_{l,i}z_{l,i})^{N+1}}\right].
 \tag{33}
\]
Then (23),(32) prove the exact original source period
\[
 \boxed{\quad
 \Phi_0(W_\beta(M))=
 N^{3r}\int_{(\Gamma^r)^3}\mathcal K(M).
 \quad}\tag{34}
\]
The cyclic order of the three kernels is fixed. Every original
crossing, Cartan factor, prefix endpoint, and external source
line remains in the matrices defining them. Further resolutions
expand \(B_-\), \(S\), or \(E_\Sigma^d\) into a finite word without
altering (34). There is no replacement of a cap by an infinite
series or of the pointed source by a normalized trace.

On the compact cycle the incidence denominators stay nonzero.
At each fixed \(N,m\) the form has a Laurent expansion in \(u\)
with a finite principal part, smooth on that cycle. Thus finite part and integration
commute. The original value is the integral of its full finite
part. Its individual negative coefficients and all relative
normal terms are retained. Equation (29) follows only after
the complete resolutions have performed their contractions.

The same formulas apply to a whole actual Casimir pair: its
reduced projector is \(P_\chi+P_{\chi^{-1}}\), which commutes
with \(T,J\) and the actual reduced word. This exact physical
pair resolution is distinct from a local geometric phase window.

## 6. Relative windows and their boundary comparison

Let \(\mathcal C\) be a compact oriented real \(2r\)-chain in
\(X^r\), possibly with boundary, on which the displayed forms
are defined. Its actual partial resolution is the matrix
\[
 P_{\mathcal C}=N^r\int_{\mathcal C}\Pi\,\nu^{[r]}.
 \tag{35}
\]
It need not be an idempotent. A restriction of (34) to three
such chains is exactly
\[
 \frac{D_N(M)}{a_N(M)}
 \operatorname{Tr}\bigl(
 P_{\mathcal C_0}J(M)P_{\mathcal C_1}B_-(M^{-1})
 P_{\mathcal C_2}J(M^{-1})\bigr).
 \tag{36}
\]
This statement retains the full finite cap and factorial dual;
it does not replace a chain by a symbolic point.

The precise opposite-polarization comparison of two windows is
\[
 \mathcal D_{\mathcal C,\mathcal D}(M)
                 =P_{\mathcal C}T(M)-T(M)P_{\mathcal D}.
 \tag{37}
\]
For the full compact resolutions it is zero. For
\(A_+=P_{\mathcal C}B_+(M)\) and
\(A_-=P_{\mathcal D}B_-(M^{-1})\), (11) gives
\(\Delta=\mathcal D_{\mathcal C,\mathcal D}B_-(M^{-1})\);
(24) is therefore its exact source-sewing correction. In
particular an assertion that the two local windows are
transported into each other has this concrete finite row to pay.

There is also an explicit boundary transgression. Suppose a
compact homotopy \(\mathcal H:[0,1]\times\mathcal C\to X^r\)
avoids the incidence divisor. Orient its side as
\([0,1]\times\partial\mathcal C\). The matrix-valued form
\(\Pi\nu^{[r]}\) is a holomorphic top form, hence closed. Stokes gives
\[
 P_{\mathcal C_1}-P_{\mathcal C_0}
 =N^r\int_{[0,1]\times\partial\mathcal C}
                       \mathcal H^*(\Pi\nu^{[r]}).
 \tag{38}
\]
The sign is positive because
\(\partial([0,1]\times\mathcal C)=
\mathcal C_1-\mathcal C_0-[0,1]\times\partial\mathcal C\).
Changing both windows in (37) consequently changes its defect
by the first boundary matrix times \(T\), minus \(T\) times
the second boundary matrix. All these statements hold
meromorphically in \(M\) and coefficientwise in its normals.
A noncompact homotopy additionally requires its end chains
and their estimates; none is supplied by compact Stokes.

If \(\Gamma^r=\mathcal C+\mathcal C^{\rm comp}\) as chains,
then \(P_{\mathcal C^{\rm comp}}=I-P_{\mathcal C}\) exactly.
Expanding each full resolution in (34) retains every
complementary product in (36). There is no implicit removal
of the other seven products after choosing three windows.
Relative products can have a double meridian pole and their
finite parts can contain second derivatives: the closed
cancellations in (22),(29) do not remove them separately.

This is an actual integral correspondence with a specified
relative defect. It is not yet a pointwise map or a homology
isomorphism between selected geometric relative cycles.

## 7. The geometric loxodromic argument remains a separate continuation

The factorization (10) explains exactly which polarization
change is implemented at the finite source level. The first
turnover takes \(F_\Sigma=0\) to \(E_\Sigma=0\) on controlled
classical charts, as Z records. The subsequent \(E_\Sigma^{N-1}\)
and quotient are retained operators, not a presumed classical
coordinate change of those cycles. Their full kernels occur in
(33). No uniform large-\(N\) symbol for them is asserted here.

For a scalar argument \(z\) on a compact loxodromic branch
\(|z|>1+\delta\), the normalization has the exact formula
\[
 D_N(z)^{-1}=(z-z^{-1})z^{-N}(1-z^{-2N})^{-1}.
 \tag{39}
\]
The last factor is \(1+O((1+\delta)^{-2N})\), with fixed
derivatives bounded by the corresponding polynomial powers of
\(N\). Thus the character \(-N\Log z\) and the nonzero factor
\(z-z^{-1}\) remain. The reciprocal branch uses the same
\(D_N\). This is a scalar statement; it neither evaluates
\(J\)'s coherent kernel at a geometric point nor turns it into
a unit-amplitude transport.

All physical root weights \(\chi\) in (20) lie on the unit
circle. A loxodromic geometric total-product eigenvalue is not
one of those physical eigenvalues at \(M=1\). Continuing a
source phase or a relative cycle to that argument still needs
its actual analytic comparison. In particular neither (27)
nor compact source equality makes the window defect (37) zero.
Acyclicity of the polar residue does not cancel the secondary
first-normal source (30), and does not prove addition or
nonvanishing of two geometric contributions.

The result is the explicit opposite-polarization operator
(9), its source normalization (18), compact paired period
(34), root normal algebra (26)--(30), and relative boundary
row (37)--(38). These leave the geometric occurrence and
relative-cycle estimates as identifiable additional work.

## Complete proof directs

* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* P: notes/research_reduced_casimir_pair_localizer.md,
  SHA256 e5307ed7e424ba181db9b73f8473342a094ed85caf0b521b4aa965bb78e3c4ea.
* Z: notes/research_central_resolvent_compact_source_symmetry.md,
  SHA256 cad44400a6c2af18972d363d6e69e61c72eb60b7499c43fba9545fe45f93ff9a.

All three complete directs were freshly read nontruncated in
this active author sequence. Every used implication was checked.
Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.

