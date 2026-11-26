# The external highest-weight cut and full Hermite boundary recovery

Private written comparison, 14 November 2026. The external
`rivin-jones` formula fixes one highest-weight input and output and
traces the remaining heads with its specified \(K\). This note
transports that actual functional, rather than replacing it by an
unmarked trace. It then recovers every coefficient of a canonical
Newton boundary polynomial by explicit inserted versions of the same
functional. The recovery includes the first derivatives at all double
Casimir roots, at every level \(N\ge2\).

The boundary polynomial recovered here has degree below \(N\) in each
independent pair coordinate. Products of several free incidences at
one vertex must be retained as ordinary polynomials after those
incidences have been recovered separately. A single pair operator
does not retain a multiple of \(P_N\).

## 1. Parameters, basis map, and the literal cut

Use the external finite contraction at
[rivin-jones commit e956fb919ac7d1bbc7cb3d3873fbac993feb94b7](https://github.com/igorrivin/rivin-jones/tree/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7),
specified in `docs/MATHEMATICS.md` and `python/rivin_jones/r_matrix.py`.
The written source snapshot was read at
`/private/tmp/rivin-jones-review-20261113`; no external code was executed.
Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad
 A_N=q^{-1/2},\quad t=A_N^2=q^{-1},\quad
 \eta=(-1)^d.
 \tag{1}
\]
The square root in (1) is the displayed exponential
\(A_N=e^{-\pi i/(2N)}\). It is not an arbitrary square-root choice.
In the external basis \(u_0,\ldots,u_d\),
\[
 K_{\rm ext}u_i=t^{d-2i}u_i.
\]
Let \(|0\rangle,\ldots,|d\rangle\) be the original balanced
physical basis of the [finite Newton calculus](../papers/newton-calculus/finite.tex).
The [exact local crossing adapter](research_rivin_jones_local_crossing_adapter.md) is
\[
       T u_i=q^{-i(i-1)/2}|d-i\rangle.
 \tag{2}
\]
Its local coefficient comparison gives
\[
 T K_{\rm ext}T^{-1}=K,\qquad
 (T\otimes T)R_{{\rm ext},\pm}(T\otimes T)^{-1}=R_{\mp}.
 \tag{3}
\]
Thus the physical braid word has every crossing sign reversed.
There is no change of word order in (3). The first equality is also
immediate from \(d-2(d-i)=-(d-2i)\). The monomial factors in (2)
have modulus one and are retained in all uncontracted wires.

For any operator \(X\) on \(b\) external heads, with no invariance
assumption, define its prescribed external cut by
\[
 L_{{\rm ext},b}(X)=
 \operatorname{Tr}\left[
   (P_0\otimes K_{\rm ext}^{\otimes(b-1)})X\right],
 \qquad P_0=u_0u_0^*.
 \tag{4}
\]
Here \(u_0^*\) is the coordinate dual row; no Hermitian pairing is
being substituted for the original contraction. Formula (4) is
exactly the sum over diagonal tail colors in the external source.
If
\[
             Y=T^{\otimes b}X(T^{-1})^{\otimes b},
\]
then cyclicity of the full matrix trace proves the unrestricted
functional identity
\[
 L_{{\rm ext},b}(X)=
 \operatorname{Tr}\left[
        (P_d\otimes K^{\otimes(b-1)})Y\right],
 \qquad P_d=|d\rangle\langle d|.
 \tag{5}
\]
Indeed \(TP_0T^{-1}=P_d\): the two nonzero scalar factors cancel.
This proves the dual observation as well as the operator adapter.

## 2. When the lowest-head observation equals the original cut average

Suppose \(Y\) commutes with the total physical \(E,F,K\). Treat
the last \(b-1\) heads as one tail module, with generators
\(E_B,F_B,K_B\), and put
\[
                      C=\operatorname{Tr}_B(K_B Y).
 \tag{6}
\]
The coproducts are the original ones:
\[
 E_{1B}=E_1K_B+E_B,\qquad
 F_{1B}=F_1+K_1^{-1}F_B,\qquad K_{1B}=K_1K_B.
\]
Taking the unweighted partial trace of
\([Y,E_1K_B+E_B]=0\) gives \([C,E_1]=0\), since the
partial trace of \([Y,E_B]\) vanishes and a tail-only factor
can be moved cyclically inside that partial trace.

For the lowering equation, take the \(K_B\)-weighted partial
trace. Conservation of \(K_1K_B\) gives
\[
                 YK_1^{-1}=K_1^{-1}K_B^{-1}YK_B.
\]
It follows that
\[
 \operatorname{Tr}_B K_B[Y,K_1^{-1}F_B]
  =K_1^{-1}\operatorname{Tr}_B
       (YK_BF_B-K_BF_BY)=0.
\]
The other term gives \([C,F_1]=0\). Likewise \(C\) commutes
with \(K_1\). The \(N\) eigenvalues of \(K_1\) are distinct,
and all adjacent lowering coefficients are nonzero. Therefore
\(C=cI\): first it is diagonal, and then commuting with the
lowering arrows makes its diagonal entries equal.

Let the original physical all-head cut average be
\[
 \Phi_b(Y)=\frac1N\operatorname{Tr}
         [(I\otimes g^{\otimes(b-1)})Y],
                  \qquad g=\eta K.
 \tag{7}
\]
Equations (5)--(7) now give
\[
                   L_{{\rm ext},b}(X)=\eta^{b-1}\Phi_b(Y).
 \tag{8}
\]
For \(b=1\), an invariant operator is already scalar and the same
identity holds. No nonzero quantum dimension is divided out.

Equation (5), rather than (8), remains the formula for arbitrary
inserted exteriors that fail the intertwining condition. In
particular, a highest or lowest coordinate projector must not be
replaced by the normalized identity on such an exterior. This is the
same distinction retained by the exact source formulas in
[the complete multiplicity module](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_source_multiplicity_module.md),
Section 4: its scalar identity is proved on actual intertwiners,
while its unrestricted marked contraction remains a matrix.

## 3. Exact framing of a closed knot braid

Let \(w\) denote the writhe of an external \(b\)-strand word, and
let \(Y\) be its physical sign-reversed word under (3). The external
normalization multiplies (4) by
\[
             A_N^{-w d(d+2)}=q^{w d(d+2)/2}.
 \tag{9}
\]
The original physical enhancement with pivot \(g\) is
\(\theta=\eta q^{d(d+2)/2}\). This follows directly from the first
column of the actual Newton crossing matrix in
[the source compiler](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md),
Section 1: the coefficient of \(e_k\) in \(R\) is
\(\kappa(-1)^kq^k\), with \(\kappa=q^{d^2/2}\).
Since \(\phi_N(e_k)=\delta_{k,d}\),
\[
                  \phi_N(R)=\kappa\eta q^d
                                =\eta q^{d(d+2)/2}.
\]
The inverse crossing has conjugate coefficients in the real Newton
basis and gives the reciprocal enhancement. Replacing the physical
pivot \(g=\eta K\) by \(K\) removes its factor \(\eta\), giving
\(\alpha=q^{d(d+2)/2}\). Thus the pivot sign is checked in the
same original polynomial source used below.

If the braid closure is a knot, its permutation is a \(b\)-cycle.
Each positive or negative braid generator is an odd permutation,
so \(w\equiv b-1\pmod2\). The physical mirror word has writhe
\(-w\). Its original zero-framing correction is therefore
\[
                 \theta^{w}=\eta^{b-1}q^{w d(d+2)/2}.
 \tag{10}
\]
Combining (8)--(10) proves equality of the normalized external
knot scalar with the normalized original physical scalar of that
marked mirror word. This keeps the exact phase, not just its modulus.
It makes no claim about a multi-component normalization not specified
by the external source.

## 4. The full canonical pair boundary from prescribed inserted cuts

Let \(\Omega\) be the original physical pair Casimir and define
the explicit external operator
\[
        \Omega_{\rm ext}=(T\otimes T)^{-1}\Omega(T\otimes T).
 \tag{11}
\]
The full pair-commutant theorem of the finite Newton calculus gives
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 f\longmapsto f(\Omega_{\rm ext})
 \tag{12}
\]
as an injective realization of the complete transported pair algebra.
It includes the double-root nilpotents. For every canonical pair
state \(X=f(\Omega_{\rm ext})\), write its unique polynomial as
\[
              f(z)=\sum_{i=0}^{d}a_i e_i(z),\qquad \deg f<N.
\]
The external cut \(L_{{\rm ext},2}\) will be denoted by \(L\).
For every polynomial \(h\), equations (8) and Newton duality give
\[
 L\bigl(h(\Omega_{\rm ext})X\bigr)=\eta\phi_N(hf),
       \qquad \phi_N(e_i e_j)=\delta_{i+j,d}.
 \tag{13}
\]
Consequently the actual coefficient formula is
\[
             a_i=\eta L\bigl(e_{d-i}(\Omega_{\rm ext})X\bigr),
                    \qquad 0\le i<N.
 \tag{14}
\]
This proves canonical boundary recovery from a specified module and
its specified dual observations. It does not infer that boundary
from the single scalar \(L(X)\). Every observation in (14) uses
the same highest-head projector and external tail pivot as (4),
with the displayed Casimir coupon inserted before that closing.

For \(r\) independent pair-algebra factors the tensor formula is
equally exact. If
\[
 X=\sum_{\mathbf i}a_{\mathbf i}
       \bigotimes_{j=1}^{r}e_{i_j}(\Omega_{{\rm ext},j}),
\]
then
\[
 a_{\mathbf i}=\eta^r L^{\otimes r}
       \left[\left(\bigotimes_{j=1}^{r}
                     e_{d-i_j}(\Omega_{{\rm ext},j})\right)X\right].
 \tag{15}
\]
The input space of (15) is the tensor product of the independent
pair algebras. A general multihead braid intertwiner is not being
declared a member of that smaller space merely from its total Hopf
invariance.

## 5. Explicit reconstruction of every double-root normal

For a double root \(c\) of \(P_N\), put
\[
 Q_c(z)=\frac{P_N(z)}{(z-c)^2},\qquad a_c=4-c^2\ne0.
\]
The original Chebyshev identities give
\(Q_c(c)=N^2/a_c\) and \(Q_c'(c)/Q_c(c)=c/a_c\).
Define canonical polynomials
\[
 E_c(z)=\frac{Q_c(z)}{N^2}\{a_c-c(z-c)\},\qquad
 V_c(z)=\frac{a_c}{N^2}(z-c)Q_c(z).
 \tag{16}
\]
At \(c\), their value/derivative pairs are respectively \((1,0)\)
and \((0,1)\); at every other double root both pairs vanish.
They also vanish at the possible simple root. Thus, in the full
algebra,
\[
 E_c^2=E_c,\qquad E_cV_c=V_c,\qquad V_c^2=0.
 \tag{17}
\]
Distinct components annihilate one another. These identities follow
from the stated jets and divisibility by \(P_N\) with its actual
multiplicities.

The original Hermite closing formula, combined with (13), is
\[
 L(f(\Omega_{\rm ext}))
   =\sum_{c\ {m double}}
        \{a_c f'(c)-c f(c)\}
       +\mathbf1_{N\ {m odd}}f(-2).
 \tag{18}
\]
There is no parity sign on the double terms: the factor \(\eta\)
in (13) cancels the factor \(\eta\) in the physical Hermite trace.
The odd-level simple term also has \(\eta=1\).

Applying (18) to the two coupons (16) gives the explicit full-jet
recovery formulas
\[
 \begin{split}
 f(c)&=\frac{L(V_c(\Omega_{\rm ext})X)}{a_c},\\
 f'(c)&=\frac{L(E_c(\Omega_{\rm ext})X)+c f(c)}{a_c}.
 \end{split}
 \tag{19}
\]
At odd \(N\), let
\[
                    E_{-2}(z)=\frac{P_N(z)}{N^2(z+2)}.
\]
Because \(P_N'(-2)=N^2\), this is the idempotent of the simple
root, and
\[
                    f(-2)=L(E_{-2}(\Omega_{\rm ext})X).
 \tag{20}
\]
Finally the recovered canonical polynomial is exactly
\[
 f(z)=\sum_{c\ {m double}}
           \{f(c)E_c(z)+f'(c)V_c(z)\}
       +\mathbf1_{N\ {m odd}}f(-2)E_{-2}(z).
 \tag{21}
\]
Both sides have degree below \(N\) and identical complete Hermite
data, which proves (21). For example the nonzero element \(V_c\)
has zero value at every spectral root, yet
\(L(E_c(\Omega_{\rm ext})V_c(\Omega_{\rm ext}))=a_c\ne0\).
This shows directly where an evaluation-only reconstruction would
lose a genuine part of the external source.

## 6. Scope of the recovered boundary

Equations (14), (19), and (20) recover all canonical pair data,
including every first normal, from explicit finite contractions.
They use Casimir coupons, not only crossing powers. At composite
levels crossing eigenvalues can coincide at different Casimir nodes;
recovery from crossing powers alone is not asserted.

If a free vertex has several incident canonical boundary factors,
its retained ordinary polynomial is their product before reduction.
Its degree can exceed \(N-1\). Passing first to one pair matrix
identifies this polynomial with its remainder modulo \(P_N\), and
none of the observations above can undo that loss. The incidence
factors, or their full independent coefficient tensor (15), must be
retained before their free coordinates are identified. This is an
exact requirement on the boundary representation, not an asymptotic
estimate.

The external scalar routine alone does not return the inserted
observations (14). The equations specify the additional boundary
contractions required for an exact mathematical correspondence; no
claim of an implemented boundary API is made here. No volume
asymptotic or geometric saddle selection is inferred from the finite
correspondence.

Only written mathematics is used. No numerical evaluation, test,
import, compilation, public-document edit, or frozen-proof edit was
performed.
