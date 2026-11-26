# A braid-compatible retraction onto the original saturated source

24 November 2026. Written research proof.

The divided-current source equation has a retraction that commutes with
every original regular braid. In the coherent corner coordinates this
retraction is an explicit finite polynomial in the actual middle divided
currents. Its source and complementary spaces therefore remain separate
through overlapping crossings and through regular linear cup/cap maps.

A positive metric makes this separation orthogonal, agrees with the
physical metric on the source, and retains the original polynomial
input/closing budget. A second specified metric gives a uniform
divided-current repair gap for the entire source equation. These
metrics have different budget statements, made explicit below.
Neither estimates the scalar carried by the restricted word nor
identifies a geometric contributing saddle.

## 1. The physical root source and its full divided currents

Use the actual conventions of [D,K,M,C]. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad x=q^d=-q^{-1},\quad \varrho=q-q^{-1}.
 \tag{1}
\]
On the original orthonormal head \(V=\mathbb C^N\),
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle,
 \quad H|a\rangle=(d-2a)|a\rangle .
 \tag{2}
\]
Missing endpoint arrows vanish. Ordered totals use
\(E_{12}=E_1K_2+E_2\), \(F_{12}=F_1+K_1^{-1}F_2\),
\(K_{12}=K_1K_2\), and additive unrolled \(H\).
All norms and adjoints below use physical Euclidean coordinates unless
a metric is specified.

For \(b=2k\) heads let \(T_b=V^{\otimes b}\) and define
\[
 \mathcal Z_b=\ker E_b\cap\ker F_b\cap\ker(K_b-I),\qquad
 \mathcal I_b=\mathcal Z_b\cap\ker H_b.
 \tag{3}
\]
The unrolled weight is retained: \(\mathcal Z_b\) includes all its
weights \(H_b=2Nj\), whereas \(\mathcal I_b\) is its weight-zero part.
Let \(\mathcal S_b\subset\mathcal I_b\) be the saturated specialization
of the regular generic invariant tensors, in the actual balanced lattice.
It is the original deformable source, not the whole root invariant space.

Define the full first-normal currents by generic division before
specialization:
\[
 J_{E,b}=\left[\frac{E_b(\zeta)^N}{1-\zeta^{2N}}\right]_q,
 \qquad
 J_{F,b}=\left[\frac{F_b(\zeta)^N}{1-\zeta^{2N}}\right]_q.
 \tag{4}
\]
Their ordered divided coproduct is regular by [K]. Every nonzero local
factorial index is less than \(N\). The scalar relating either current
to its divided power is the same:
\[
 \alpha_N=
 \frac{Nq^{-N(N-1)/2}}{(1-Q)^N}.
 \tag{5}
\]
Thus these are specified physical matrices at every level, including
even and composite levels; (4) does not divide a zero root matrix.

Both currents preserve \(\mathcal Z_b\). Here is the mixed-commutator
check needed for this assertion. For the standard generator
\(e_\zeta=E/(\zeta-\zeta^{-1})^2\), the elementary finite identity is
\[
 [e_\zeta^{[n]},F]
  =e_\zeta^{[n-1]}
    \frac{\zeta^{n-1}K-\zeta^{1-n}K^{-1}}
         {\zeta-\zeta^{-1}}.
 \tag{6}
\]
It follows by summing the \(n\) ordinary commutators before dividing
by \([n]_\zeta!\). There is an analogous identity for
\([e_\zeta,F^{[n]}]\), with a Cartan coefficient multiplying
\(F^{[n-1]}\). At \(n=N\), specialization and (5) show that
\([J_{E,b},F_b]\) factors through \(E_b^{N-1}\) and that
\([E_b,J_{F,b}]\) factors through \(F_b^{N-1}\).
Those factors kill \(\mathcal Z_b\), since \(N\ge2\); the intervening
Cartan operators preserve the ordinary kernels. Each current commutes
with its own ordinary generator, and its Cartan character is
\(Q^{\pm N}=1\). This proves preservation of all three kernels in (3),
including \(N=2\). The unrolled weights change by \(+2N,-2N\).

The actual divided commutation calculation [D] on the full physical
\(K_b=1\) sector gives
\[
 [J_{E,b},J_{F,b}]=-NH_b.
 \tag{7}
\]
Consequently on \(\mathcal Z_b\) the operators
\[
 e=J_{E,b}/N,\qquad f=-J_{F,b}/N,\qquad h=H_b/N
 \tag{8}
\]
satisfy exactly \([e,f]=h\), \([h,e]=2e\), \([h,f]=-2f\).
No physical Hermitian relation between these operators is assumed.

## 2. A full-current retraction commuting with the braid word

On the weight-two part of \(\mathcal Z_b\), put
\[
 R=\sum_{j=0}^{k-2}
       \frac{(-1)^j f^{j+1}e^j}{(j+1)!(j+2)!}.
 \tag{9}
\]
For \(k=1\) that weight space is zero and the sum is empty.
Indeed \(|H_b|\le2k(N-1)<2kN\), so the possible weights of \(h\)
lie between \(-2(k-1)\) and \(2(k-1)\).
For a weight-two vector \(v\), the ordinary relations give
\[
 ef^{j+1}e^jv=f^{j+1}e^{j+1}v
                     +(j+1)(j+2)f^je^jv.
 \tag{10}
\]
The successive terms telescope to \(eR=I\). The final term vanishes
by the displayed weight bound. Therefore on \(\mathcal I_b\)
\[
 \boxed{\quad
 \Pi_b=I-Re
       =I+\sum_{m=1}^{k-1}
          \frac{J_{F,b}^{m}J_{E,b}^{m}}
               {N^{2m}m!(m+1)!}.
 \quad}
 \tag{11}
\]
It satisfies \(e\Pi_b=0\), is the identity on \(\ker e\), and hence
\(\Pi_b^2=\Pi_b\). The complete source theorem [D], on the full
invariant tensor rather than only its extraction, says
\[
 \boxed{\quad
 \operatorname{ran}\Pi_b
   =\mathcal I_b\cap\ker J_{E,b}=\mathcal S_b.
 \quad}
 \tag{12}
\]
Its redundant \(J_F\) equation is retained. For \(b=2\), the invariant
space is the original cup line and (11) is the identity. The unit
space at \(b=0\) also has identity retraction.

Every original regular generic signed braid intertwines the total
generic \(E,F,K,H\). Taking a power, dividing by the common scalar
in (4), and specializing gives commutation with both full currents.
It follows term by term in (11) that
\[
                  R_i^{\pm1}\Pi_b=\Pi_bR_i^{\pm1}
                         \quad\hbox{on }\mathcal I_b.
 \tag{13}
\]
The same conclusion holds for any specified regular generic linear
Hopf, unrolled-weight intertwiner, including the original interval
Casimir polynomials and regular circle coupons. It retains their actual
confluent Casimir data; no repeated-root derivative has been deleted.

This is stronger than knowing only that a braid preserves
\(\mathcal S_b\): its complementary space \(\ker\Pi_b\) is preserved
as well. For any braid word, a complementary component cannot return
to the source under a later overlapping crossing.

## 3. The explicit projector in the coherent corner coordinates

Let \(b=2k\ge4\), \(W=V^{\otimes(2k-2)}\),
\(D=(k-1)d\), and let \(W_D\) be its physical central-degree space.
The coherent corner isomorphism [C] is
\[
 \mathscr F_b:\mathcal I_b\longrightarrow W_D,
 \qquad
 \mathscr F_b\Phi=c_{\rm edge}\,q_0\Phi,
 \qquad
 q_0\Phi=\frac{x^{2d}}{N^2}\Phi_{0,W,d}.
 \tag{14}
\]
Here \(c_{\rm edge}\ne0\) is the exact original constant of [C].
Formula (14) also defines the coefficient extraction on every weight
of \(\mathcal Z_b\). In fact it extends to an isomorphism
\(q_0:\mathcal Z_b\to\ker(K_W-I)\), with all unrolled weights retained.

Here is an elementary proof of this larger assertion. Let \(A=V\otimes V\)
and \(v=|d,0\rangle\). For \(0\le a,b<N\), the actual coproduct gives
\[
 F_A^bv=x^b(Q;Q)_b|d,b\rangle.
 \tag{14a}
\]
In \(E_A^aF_A^bv\), the unique term using only first-head lowerings
is a nonzero multiple of \(|d-a,b\rangle\). Every other term has
second occupation less than \(b\). Ordering by that occupation proves
that the \(N^2\) vectors \(E_A^aF_A^bv\) are a triangular basis of
\(A\). The ordinary root quantum algebra acting on even blocks has
\(E^N=F^N=0\), \(K^N=1\). Reordering its elementary commutator shows
that its induced left module \(U/U(K-I)\) is spanned by the same
\(N^2\) monomials. The map sending its cyclic vector to \(v\) is
therefore an isomorphism. For every even middle block this gives
\[
 \operatorname{Hom}_{U}(A,W)\longrightarrow\ker(K_W-I),
                         \qquad f\longmapsto f(v)
                         \quad\hbox{bijectively}.
 \tag{14b}
\]
The ordinary cup/cap snake identities in [M] identify the left-hand
space with \(\mathcal Z_b\), without imposing an unrolled-weight-zero
condition. Literal currying gives \(f(v)=q_0\Phi_f\) just as in [C].
Since the two extracted end weights cancel, \(q_0H_b=H_Wq_0\).
This proves the full graded isomorphism and includes all endpoint
arrows; it assumes no semisimple quantum decomposition.

Both full currents have a definite parity under this extraction:
\[
 \boxed{\quad
 q_0J_{E,b}=(-1)^dJ_{E,W}q_0,
 \qquad q_0J_{F,b}=(-1)^dJ_{F,W}q_0
                         \quad\hbox{on }\mathcal Z_b.
 \quad}
 \tag{15}
\]
We give a direct ordered-coproduct proof, without differentiating the
root extraction. Put \(v=\Phi_{0,W,d}\). The ordinary invariant
equations at the two ends imply
\[
 \Phi_{a,W,d}=\frac{(-1)^aE_W^a}{(Q;Q)_a}v,
 \qquad
 \Phi_{0,W,d-a}=\frac{F_W^a}{(Q;Q)_a}v,
                      \quad 0\le a<N.
 \tag{16}
\]
For example the first recursion is
\((1-Q^{a+1})\Phi_{a+1,W,d}+E_W\Phi_{a,W,d}=0\).
The second is
\((1-Q^{a+1})\Phi_{0,W,d-a-1}=F_W\Phi_{0,W,d-a}\).
They use \(K_b\Phi=\Phi\), not the additional condition \(H_b=0\).

In a term of the divided \(E_b^{[N]}\) coproduct contributing to
output end colors \((0,d)\), the last local exponent is zero.
If the first exponent is \(a\), then \(0\le a<N\), and the middle
exponent is \(N-a\). For \(a>0\), move the middle Cartan power
past the first string in (16). The remaining middle operator contains
\(E_W^{N-a}E_W^a=E_W^N=0\) at the root; all the local factorials
in this mixed term are nonzero. Thus every mixed term vanishes.
The \(a=0\) term is the full middle divided current times
\(K_{\rm last}^N=(x^{-1})^N=(-1)^d\).
The common normal factor is (5), proving the first identity (15).
For \(F_b^{[N]}\), output first color zero forces its first exponent
zero. If the last exponent is positive the second string in (16)
gives \(F_W^N=0\); the surviving term retains
\(K_{\rm first}^{-N}=x^{-N}=(-1)^d\). This proves the second
identity, with the same sign at even as at odd levels.

The signs in (15) cancel in every paired current product. Hence
the transported retraction is the explicit middle polynomial
\[
 \boxed{\quad
 P_b:=\mathscr F_b\Pi_b\mathscr F_b^{-1}
 =I_{W_D}+\sum_{m=1}^{k-2}
       \frac{J_{F,W}^{m}J_{E,W}^{m}}
            {N^{2m}m!(m+1)!}.
 \quad}
 \tag{17}
\]
The missing \(m=k-1\) term is zero: it would lower middle degree
\(D=(k-1)(N-1)\) by \((k-1)N>D\).
In particular (17) is empty at four heads. Its range is precisely
\[
 \mathscr F_b\mathcal S_b
   =\ker(J_{E,W}:W_D\longrightarrow W_{D-N}),
 \tag{18}
\]
with zero target when appropriate, as already identified in [C,D].

If \(B_i=\mathscr F_b R_i\mathscr F_b^{-1}\), then
\[
                         [P_b,B_i^{\pm1}]=0.
 \tag{19}
\]
This includes the two actual boundary Casimir braid polynomials in
[C], as well as every interior crossing. Formula (17) has the same
finite-current shape as the earlier prefix projector [D]. The proof
here establishes its braid commutation in this specified corner chart;
it does not identify two different extraction charts without their
actual coordinate change.

## 4. Linear gluing and its tensor-product limit

Let \(T_\zeta:T_b(\zeta)\to T_{b'}(\zeta)\) be any specified regular
generic linear Hopf intertwiner preserving unrolled weight. Then its
root map intertwines both full divided currents. The finite sums (11)
can be padded with zero terms to a common length, because powers beyond
each physical weight range vanish. Consequently
\[
                  T\Pi_b=\Pi_{b'}T
                        \quad\hbox{on }\mathcal I_b.
 \tag{20}
\]
Thus an ordinary cup insertion, ordinary cap contraction, regular
linear sewing, or composition of these with actual braids carries
source to source and complement to complement. On nontrivial corner
packets the transported map
\(\widetilde T=\mathscr F_{b'}T\mathscr F_b^{-1}\) obeys
\(\widetilde T P_b=P_{b'}\widetilde T\).
The marked row is not a Hopf map and is handled by the original
closing in the next section, rather than by (20).

This is naturality for a linear map on the complete incoming packet.
It is not a monoidal identity
\(\Pi_{b+b'}=\Pi_b\otimes\Pi_{b'}\). Nontrivial ordinary divided-
\(\mathfrak{sl}_2\) factors can couple to a trivial factor. Therefore
one cannot independently project two arbitrary inputs before a binary
tensor operation and infer that their full coupled source is retained.
One first forms the complete incoming tensor and uses its full projector.

## 5. A compatible positive metric with the original closing

On each corner packet define \(Q_b=I-P_b\) and
\[
 G_b=P_b^\dagger P_b+Q_b^\dagger Q_b,
 \qquad \|v\|_{G_b}^2=\|P_bv\|^2+\|Q_bv\|^2.
 \tag{21}
\]
This is an explicit metric of the level and fixed source representation,
independent of the word or its unknown scalar. The elementary triangle
inequality gives
\[
 G_b\succeq\tfrac12 I,\qquad
 G_bP_b=P_b^\dagger P_b=P_b^\dagger G_b.
 \tag{22}
\]
Thus source and complement are orthogonal, and \(P_b\) is their
orthogonal projection in this metric. On either subspace separately
the metric equals the original physical metric. No upper polynomial
bound for \(G_b\), its condition number, or \(\|P_b\|\) is asserted.

For every intertwiner \(A\) with \(AP_b=P_{b'}A\), one has
\[
 \|Av\|_{G_{b'}}^2
   =\|AP_bv\|^2+\|AQ_bv\|^2
   \le\|A\|_{\rm physical}^2\|v\|_{G_b}^2.
 \tag{23}
\]
In particular all actual reduced braid matrices satisfy
\(\|B_i^{\pm1}\|_{G_b}\le\|B_i^{\pm1}\|_{\rm physical}\).
This statement does not make the physical crossing norm small.

Keep the exact corner input and literal original row [C]:
\[
 z_{\rm in}=c_{\rm edge}|d\rangle\otimes
                  p^{\otimes(k-2)}\otimes|0\rangle,
 \qquad
 \lambda_D=c_{\rm edge}^{-1}\langle0,d|
       (I\otimes\ell^{\otimes(k-2)}\otimes I).
 \tag{24}
\]
All turn powers, pivots, framing and any original external scalar
\(\chi_N\) remain as prescribed. This literal row already annihilates
the full divided currents:
\[
 \boxed{\quad
 \lambda_DJ_{E,W}=\lambda_DJ_{F,W}=\lambda_DH_W=0,
 \qquad \lambda_DP_b=\lambda_D.
 \quad}
 \tag{24a}
\]
To prove the current identities on the full physical middle tensor,
put \(A=V\otimes V\). The map
\(L_{\rm int}=I\otimes\ell^{\otimes(k-2)}\otimes I:W\to A\)
is a regular generic Hopf map. Generic division by the same normal
factor therefore gives
\(L_{\rm int}J_{E,W}=J_{E,A}L_{\rm int}\), and likewise for \(F\).
The pair row \(\langle0,d|J_{E,A}\) would require input degree
\(d+N=2N-1>2d\), and \(\langle0,d|J_{F,A}\) would require degree
\(d-N=-1\). Both rows are zero at every \(N\ge2\).
The unrolled equation follows because that pair row has weight zero
and the ordinary caps preserve \(H\). Formula (17) now proves the
last identity in (24a) on all of \(W_D\).
This argument concerns the row after the proved whole invariant-tensor
reduction [C]; it does not assert that the raw marked cap \(m\) is a
Hopf map.

The actual cup source satisfies \(P_bz_{\rm in}=z_{\rm in}\).
Commutation (19) and (24a) show, for every original word \(B\),
\[
 \lambda_D BQ_b=0,\qquad
 \chi_N\lambda_D Bv=\chi_N\lambda_D BP_bv
                              \quad\hbox{for every }v\in W_D.
 \tag{25}
\]
Thus the unchanged original closing sees no complementary component,
even for an arbitrary root packet input. This is a global invariant
source quotient, rather than a local cap-null quotient through an
untransported neighboring crossing.

For any physical row \(\lambda\), orthogonality in (21) gives the
exact dual identity
\[
 \|\lambda P_b\|_{G_b^*}
   =\|\lambda|_{\operatorname{ran}P_b}\|_{\rm physical,*}
   \le\|\lambda\|_{\rm physical}.
 \tag{26}
\]
Indeed its value depends only on the source component, and its supremum
is already attained by allowing only that component. Applying [C]'s
exact physical boundary product yields
\[
 \boxed{\quad
 \|z_{\rm in}\|_{G_b}\,
 \|\lambda_D\|_{G_b^*}
       \le\|z_{\rm in}\|\,\|\lambda_D\|=N^{k-2}.
 \quad}
 \tag{27}
\]
If \(\chi_N\) is included in the row, the bound is multiplied by
\(|\chi_N|\); no estimate for that separate original factor is implied.
The compatible source restriction therefore introduces no exponential
boundary cost and no source-to-complement-to-source excursions under
the linear word. It retains every coherent contribution inside the source.

## 6. A quantitative gap for the complete source equation

Put \(r=k-1\) and work on the full middle physical sector
\[
 \mathcal L_W=\bigoplus_{j\in\mathbb Z}W_{H_W=2Nj}
             =\ker(K_W-I).
 \tag{28}
\]
Its weight-zero part is \(W_D\). On this whole sector the actual
operators \(e=J_{E,W}/N\), \(f=-J_{F,W}/N\), \(h=H_W/N\)
satisfy the ordinary relations (8), by [D]. Their possible \(h\)
weights are even integers with \(|h|\le2r-2\); in particular
\(e^{2r-1}=f^{2r-1}=0\). This is a statement about the actual
divided currents, not a new replacement module.

These matrices integrate to a specified representation
\(\rho:SU(2)\to GL(\mathcal L_W)\). One construction avoids a
complete-reducibility assumption. Send the standard complex
\(\mathfrak{sl}_2\) generators to \(e,f,h\). On \(SL_2(\mathbb C)\)
the right Maurer--Cartan form gives the matrix path equation
\(U'=d\rho(g'g^{-1})U\), with \(U(0)=I\). The bracket identities
make its curvature zero. Polar decomposition retracts this group onto
\(SU(2)\cong S^3\), so it is simply connected; flat transport is
independent of the path and respects multiplication. This constructs
\(\rho\), whose restriction to the displayed compact group is used below.
Equivalently its Gauss-cell matrices are the finite exponentials in
(32); their identities follow by differentiating the elementary
\(\mathfrak{sl}_2\) commutators. No root semisimplicity is used.

With Haar measure of total mass one, define
\[
 \mathfrak G=\int_{SU(2)}\rho(g)^\dagger\rho(g)\,dg.
 \tag{29}
\]
It is positive and invariant. Differentiating the compact generators
\(ih\), \(e-f\), \(i(e+f)\) gives
\[
                 h^{\dagger_{\mathfrak G}}=h,
                 \qquad e^{\dagger_{\mathfrak G}}=f.
 \tag{30}
\]
Thus different \(h\) weights are orthogonal for this metric. The norm
of a divided-current residual below is its norm in its actual output
weight, not a norm on an incorrectly identified copy of \(W_D\).

The metric has controlled exponential size in the physical frame.
To check this using only the actual matrices, the ordered formula
[K,(3),(5)] gives, up to phases, a nonzero \(J_E\) entry as
\(N\prod_i{a_i\brack b_i}_Q\), where each upper index is less than
\(N\). For \(J_F\) the corresponding upper indices are the final
occupations, also less than \(N\). A Gaussian polynomial has
nonnegative integer coefficients, so its absolute value on the unit
circle is bounded by the ordinary binomial coefficient. On \(n=2r\)
physical heads this proves
\[
 \|J_{E,W}\|,\|J_{F,W}\|
       \le N^{n+1}2^{nd},\qquad
 \|e\|,\|f\|\le e^{C_rN}.
 \tag{31}
\]
This bound involves no division by a small total root factorial.

Use the exact finite positive rule (38), proved below without any
metric-size estimate. Its fixed-width nodes have
\(g_\nu=\left(\begin{smallmatrix}a&b\\-\bar b&\bar a\end{smallmatrix}\right)\)
with \(|a|\ge a_{\min}(r)>0\), since every Gaussian node has
\(-1<t<1\). At each such node Gauss factorization gives
\[
 \rho(g)=\exp(-\bar b f/a)\,a^h\,\exp(be/a).
 \tag{32}
\]
Both unipotent parameters and \(\|a^{\pm h}\|\) are bounded by
width-only constants. The exponentials truncate at degree \(2r-2\).
Equations (31),(32) and the finite rule therefore imply
\[
 \max_\nu\|\rho(g_\nu)^{\pm1}\|\le e^{C_rN},\qquad
                 e^{-C_rN}I\preceq\mathfrak G\preceq e^{C_rN}I.
 \tag{33}
\]
For the lower bound keep any one positive-weight node and use its
inverse bound. Thus the construction has linear logarithmic metric
radius; exponentiating the possibly large number \(\|e\|\) was not used.

For completeness the resulting weight-zero gap can be derived
directly from (30). A highest vector \(v\), with \(ev=0\),
\(hv=mv\), has
\[
 \|f^av\|_{\mathfrak G}^2
   =a!\,m(m-1)\cdots(m-a+1)\|v\|_{\mathfrak G}^2.
 \tag{34}
\]
The commutator proves this recurrence, and positivity and termination
force \(m\) to be a nonnegative integer. All weights here are even,
so \(m=2J\), \(J\in\{0,\ldots,r-1\}\). Each such chain and its
\(\mathfrak G\)-orthogonal complement are invariant under \(e,f,h\).
Removing a highest chain and repeating yields an orthogonal sum of
these explicitly normalized chains. Matching their successive
\(e,f,h\) coefficients with the monomials of
\(\operatorname{Sym}^{2J}\mathbb C^2\) identifies each chain with that
explicit polynomial representation: in its monomial basis \(f\)
successively replaces a first coordinate by a second, and \(e\)
reverses this with the coefficients from (34). Uniqueness along the
chain fixes the group action as well. In particular its matrix
coefficients are polynomials of degree \(2J\) in the fundamental
group entries. On its weight-zero vector the normalized raising
coefficient is \(\sqrt{J(J+1)}\).

The \(J=0\) chains in \(W_D\) are exactly the actual saturated
source (18). The projector (17) is their \(\mathfrak G\)-orthogonal
projector: its range is \(\ker e\), and \(v-P_bv\) is in
\(\operatorname{im}f\), perpendicular to that kernel by (30).
Consequently, for every \(z\in W_D\),
\[
 \boxed{\quad
 \|z-P_bz\|_{\mathfrak G}
       \le\frac{1}{\sqrt2\,N}\|J_{E,W}z\|_{\mathfrak G}.
 \quad}
 \tag{35}
\]
At widths or levels with no nontrivial chain this is the identity
\(0\le0\). The formula therefore includes \(r=1\) and \(N=2\).
It is a global normal estimate for the whole divided-current source
equation, not a single marked-mode path estimate.

Every source vector is fixed by \(\rho\). Hence its
\(\mathfrak G\) norm is exactly its physical norm, and, just as in (26),
\[
 \|\lambda_D\|_{\mathfrak G^*}
   =\|\lambda_D|_{\operatorname{ran}P_b}\|_{\rm physical,*},
 \qquad
 \|z_{\rm in}\|_{\mathfrak G}
       \|\lambda_D\|_{\mathfrak G^*}\le N^{k-2}.
 \tag{36}
\]
An original \(\chi_N\) multiplies the second factor by \(|\chi_N|\).
Thus source repair uses a specified metric and the original boundary
without an exponential boundary budget. The residual in (35) is
measured in that metric; (33) does not imply a polynomial physical
singular gap. The literal row itself is also group invariant:
\(\lambda_D\rho(g)=\lambda_D\) on \(\mathcal L_W\), by (24a).

If an operator \(A\) on the full \(\mathcal L_W\) commutes with
\(e,f,h\), it commutes with \(\rho\), and integration gives
\[
                         \|A\|_{\mathfrak G}
                                    \le\|A\|_{\rm physical,\mathcal L_W}.
 \tag{37}
\]
Here the right-hand norm is explicitly the full-sector norm. A bound
known only for a central-degree matrix is not substituted for it.
The full isomorphism (14b), together with (15), supplies actual
extensions \(\widetilde B_i=q_0R_iq_0^{-1}\) on \(\mathcal L_W\).
They commute with \(e,f,h\), and restrict to the matrices \(B_i\)
on \(W_D\). The same holds for regular linear maps between widths,
since the sign in (15) is independent of the number of heads.
For the two boundary Casimirs their extended formulas are exactly
the \(L,R\) of [C,(29)] on \(K_W=1\): that endpoint derivation used
only \(K_W=1\), not \(H_W=0\). Their signed braid polynomials retain
all original Hermite data. Thus (37) applies to these actual extended
gates, with their full-sector physical norm on its right.
The separate metric \(G_b\) in (21) already gives (23) for all the
actual central packet gates from the proved commutation with \(P_b\).
No comparison losing that distinction is needed for (35),(36).

The Haar formula can also be made an exact finite positive Gram of
width-only size. After the orthogonal chain construction, every spin
is an integer \(J\le r-1\). Use Euler angles \(\phi,\psi\) on the
two diagonal circles and \(t=\cos\vartheta\) for the middle rotation.
Take \(L=2r-1\) equally spaced nodes on each circle and the \(r\)
Gauss--Legendre nodes for normalized measure \(dt/2\). Explicitly use
\(\phi_a=2\pi a/L\), \(\psi_b=2\pi b/L\), and
\[
 g(\phi,t,\psi)=
 \begin{pmatrix}e^{i\phi/2}&0\\0&e^{-i\phi/2}\end{pmatrix}
 \begin{pmatrix}\sqrt{(1+t)/2}&\sqrt{(1-t)/2}\\
 -\sqrt{(1-t)/2}&\sqrt{(1+t)/2}\end{pmatrix}
 \begin{pmatrix}e^{i\psi/2}&0\\0&e^{-i\psi/2}\end{pmatrix}.
 \tag{38a}
\]
The product weight is the normalized Gaussian weight divided by
\(L^2\). Normalized Haar measure in these Euler coordinates is the
product of the two uniform circle measures and \(dt/2\): the middle
rotation Jacobian is \(\sin\vartheta\,d\vartheta=-dt\).
Circle products
of matrix coefficients have frequencies at most \(2r-2<L\), so the
two circle sums perform their integrals exactly. The remaining terms
have matching magnetic indices. Products of their middle-rotation
coefficients are polynomials in \(t\) of degree at most
\(J+J'\le2r-2\): each coefficient is a sum of monomials in
\(\cos(\vartheta/2),\sin(\vartheta/2)\), and matching indices make
both exponents even in the product. The \(r\)-node Gaussian rule is
therefore exact. Thus for explicit positive, width-only weights,
\[
 \mathfrak G=\sum_{\nu=1}^{r(2r-1)^2}
                       w_\nu\rho(g_\nu)^\dagger\rho(g_\nu),
 \qquad w_\nu>0,\qquad\sum_\nu w_\nu=1.
 \tag{38}
\]
The Gaussian rule itself can be obtained from the monic degree-\(r\)
polynomial orthogonal to lower degrees for \(dt/2\). Its coefficients
are rational moments. Orthogonality forces its \(r\) roots to be
simple and inside \((-1,1)\): otherwise the product of its interior
sign-change factors has degree less than \(r\) and gives a
nonzero integral of fixed sign. Divide a polynomial of degree at most
\(2r-1\) by this orthogonal polynomial and interpolate the remainder
at its roots. This proves the Gaussian rule; its cardinals \(l_i\)
have weights \(\int l_i=\int l_i^2>0\). The weights sum to one.
Thus all group nodes and weights in (38) are algebraic and independent
of \(N\). The represented node matrices are algebraic too: use (32),
whose two exponentials are finite, and whose \(a^h\) has integer
physical exponents. This does not require finding an unknown
unitarizing change of basis.
The center acts trivially because the spins are integers, so the
ordinary normalized Euler rule on \(SO(3)\) equals the Haar average
here. This finite formula evaluates the same actual Gram; it introduces
no new state or positivity assumption about the marked scalar.

## 7. Exact source restriction in a linear residual compiler

There is a direct minimization consequence for a specified linear word
compiler. Allow packet spaces of different widths, actual linear maps
\(A_iP_{i-1}=P_iA_i\), and fixed input \(v_0=z_{\rm in}\) in the
source. For positive weights \(a_i,a_*\), a target \(c\in\mathbb C\),
and the unchanged original closing row \(\lambda=\lambda P_m\), consider
\[
 \mathcal E(v_1,\ldots,v_m)
   =\sum_{i=1}^m a_i\|v_i-A_iv_{i-1}\|_{G_i}^2
       +a_*|\lambda v_m-c|^2.
 \tag{39}
\]
Every vector residual splits into its orthogonal source and complement
parts. The closing term sees only the source part. Since \(Q_0v_0=0\),
\[
 \mathcal E(v)=\mathcal E(Pv)
       +\sum_{i=1}^m a_i
                    \|Q_iv_i-A_iQ_{i-1}v_{i-1}\|^2.
 \tag{40}
\]
Consequently projecting every trial packet cannot increase the energy
or any upper ball constraint \(\|v_i\|_{G_i}\le R_i\). The infimum,
with or without such balls, is exactly its restriction to source
packets; the complementary minimum is zero. By (23), the original
physical gate norm budgets also suffice in these metrics.

This is exact deletion of nonsource variables in this legitimate linear
compiler. It neither identifies its minimum with an unweighted scalar
energy nor changes the distinct nonlinear Conway quartic problem.
For a binary tensor operation the full coupled projector must be used;
its metric need not be the tensor product of the two input metrics.

## 8. What the retraction settles

[D,K] already identify the saturated source as an actual divided-current
kernel and provide its finite polynomial projector. [M] already gives
complete source coordinates and exact original boundaries. [C] already
identifies the coherent corner projection and its polynomial boundary
product. The additional points are the full-small-invariant construction
(11), braid and linear-gluing naturality, its signed current transport
(15), explicit commuting form (17), compatible metric budget (27), and
the full-source repair estimate (35) in the specified finite Gram (38).
The original corner row is itself divided-current invariant (24a),
so the complementary part is invisible to every word closing (25).

These statements concern fixed-root values. Differentiated generic
families retain their full inhomogeneous Ward equations and the
derivatives of any transported projector; the root formula does not
silently make those equations homogeneous. Arbitrary root-only coupons
without the specified regular generic lift are not covered by (20).

The construction imposes the complete value source restriction before
estimating a coherent word. Its repair gap is in \(\mathfrak G\), not
a claimed polynomial physical singular gap for \(J_E\). It gives no
sharp word energy or positive lower bound for the original marked
scalar. The remaining estimate concerns the source-projected word
recursion or gradient and its original closing. Formula (35) quantifies
distance when comparing with an unprojected trial; exact source
projection itself requires no small-current-residual premise.
The finite-exception volume statement after arbitrary short partial
fillings is unchanged by this compatibility result alone.

## Complete inputs

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| D | [All-width divided-current source projection](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_all_width_divided_source_projection.md) | 204 | dc83b5e232a3d258f516a479d7257e85b9e5663a38e166f07c6ad9ae81004a68 |
| K | [Actual six-port divided-power source kernel](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_six_port_divided_power_source_kernel.md) | 288 | e62a2612f0610f46278347db48024979c4f525ecca34c98c87048c4162c97fb0 |
| M | [Complete original source multiplicities](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| C | [Coherent marked-cap corner reduction](research_coherent_marked_cap_corner_reduction.md) | 466 | 6cf47746a43975723780aec77dc125846515b9c0115359fb1d5ce160f9858ca9 |

Only written mathematics, source reads and text/hash operations were used.
The earlier final notes, ledger and public manuscripts are unchanged.
