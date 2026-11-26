# A relative finite Fourier transition for a vanishing prefix minor

Private written proof, 18 November 2026.

The complementary entry at a simple classical prefix zero has an
explicit finite-source transition. A triangular tensor-prefix operator,
a diagonal factorial gauge and an actual finite Fourier matrix turn
its ordered quantum lift into a nonzero diagonal clock **minus an
explicit carry**. The carry has rank \(N^{m-1}\) on a prefix of \(m\)
heads. It cannot be dropped: the original complementary entry is
nilpotent, whereas the diagonal clock is invertible.

The construction retains the original probes, finite projectors and
all quantum/meridian normal terms. It also gives an exact partial
inverse and a two-endpoint source-current identity. It is a relative
prefix chart, not an invertible Bruhat factorization of the unchanged
finite head or a calculation of its geometric period.

The complete directs are E, the actual finite head; M, the classical
marked prefix correspondence; and V, the whole finite Fourier source.
The tensor-prefix splitting and the identities below are proved inline.

## 1. The classical complementary chart and its ordered finite lift

In M's convention the retained classical prefix is
\[
 P_m=H_m\cdots H_1=B_-^{-1}B_+,\qquad
 B_-=\begin{pmatrix}1&0\\-kf&k\end{pmatrix},\quad
 B_+=\begin{pmatrix}k&e\\0&1\end{pmatrix}.
 \tag{1}
\]
Thus \(P_{11}=k\) and \(P_{21}=fk\).
Suppose \(P(r)\in SL_2\) is regular, \(a(r)=P_{11}(r)\)
has a simple zero at \(r_*\), and write
\[
                         P=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}.
 \tag{2}
\]
Then \(b(r_*)c(r_*)=-1\), so \(c\) is a unit near that point.
The complementary classical factorization is explicitly
\[
 W^{-1}P
  =\begin{pmatrix}1&0\\a&c\end{pmatrix}^{-1}
     \begin{pmatrix}c&d_0\\0&1\end{pmatrix},\qquad
 W=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{3}
\]
Indeed its lower-right entry is
\((1-ad_0)/c=-b\). This chart is regular at \(a=0\).
Its pivot is \(c=fk\), not the reciprocal of the old pivot.

Use the original balanced heads \(w_0,\ldots,w_d\), where
\(d=N-1\), \(Q=q^2\), \(x_i=-M_i/q\), with E's finite arrows
\[
 K_iw_a=x_iQ^{-a}w_a,\quad
 F_iw_a=(1-Q^{a+1})w_{a+1}\ (a<d),\quad F_iw_d=0.
 \tag{4}
\]
The corresponding lowering arrows are E's \(\mathcal E_i\);
their two endpoint rows are unchanged. All statements take place
on the actual fixed-\(N\) normal germ at \(q=e^{\pi i/N}\),
\(M_i=1\). In particular
\[
                f_a=\prod_{j=1}^a(1-Q^j),\quad 0\le a<N,
 \qquad f_0=1
 \tag{5}
\]
are units. The letter \(f_a\) denotes a finite product, whereas
\(f\) in (1) is a classical prefix field.

For the first \(m\) ordered heads put
\[
 K_\Sigma=\prod_{i=1}^mK_i,\qquad
 F_\Sigma=F_1+K_1^{-1}F_2+\cdots+
                  K_1^{-1}\cdots K_{m-1}^{-1}F_m.
 \tag{6}
\]
Let \(\mathcal E_\Sigma\) be the correspondingly ordered sum
\(\mathcal E_1K_2\cdots K_m+\cdots+\mathcal E_m\).
Products of the literal triangular two-by-two matrices give
\[
 \widehat B_-=
   \begin{pmatrix}I&0\\-K_\Sigma F_\Sigma&K_\Sigma\end{pmatrix},
 \qquad
 \widehat B_+=
   \begin{pmatrix}K_\Sigma&\mathcal E_\Sigma\\0&I\end{pmatrix}.
 \tag{7}
\]
Their exact ordered quotient is
\[
 \widehat P=\widehat B_-^{-1}\widehat B_+
 =\begin{pmatrix}
 K_\Sigma&\mathcal E_\Sigma\\
 F_\Sigma K_\Sigma&F_\Sigma\mathcal E_\Sigma+K_\Sigma^{-1}
 \end{pmatrix}.
 \tag{8}
\]
The order in the lower-left entry is important. Its commuting
principal symbol is exactly the complementary entry \(c\) in (2).
Set
\[
                              C=F_\Sigma K_\Sigma.
 \tag{9}
\]
This is a specified insertion in the original tensor source.
No exact quantum Hurwitz identity for (8) is asserted. At another
braid level the insertion and its probes are transported by the
literal braid word, not reset to an unprefixed coupon.

## 2. An exact triangular splitting of the prefix raising operator

Write \(K_{\rm r}=K_2\cdots K_m\) and
\[
 F_{\rm r}=F_2+K_2^{-1}F_3+\cdots+
                       K_2^{-1}\cdots K_{m-1}^{-1}F_m.
 \tag{10}
\]
For \(m=1\), these mean \(K_{\rm r}=I,F_{\rm r}=0\).
Let \(L_1w_a=w_{a-1}\) for \(a>0\), \(L_1w_0=0\), be the
literal unilateral shift. Define
\[
 Z=x_1^{-1}L_1F_{\rm r},\qquad
 S=\sum_{j=0}^d\frac{Z^j}{f_j}.
 \tag{11}
\]
Since \(Z^N=0\), \(S\) is a finite unipotent matrix. Its exact inverse is
\[
                  S^{-1}=\sum_{j=0}^d
                         \frac{(-1)^jQ^{j(j-1)/2}Z^j}{f_j}.
 \tag{12}
\]
For a direct check, the scalar series
\(\sum z^j/f_j\) satisfies \(A(Qz)=(1-z)A(z)\) modulo \(z^N\);
the series in (12) has the reciprocal equation. Their product is
one modulo \(z^N\). Substitute \(z=Z\).

More concretely, for every vector \(v\) on the remaining heads,
\[
              S(w_a\otimes v)
                 =\frac{F_\Sigma^a}{f_a}(w_0\otimes v),
                       \qquad 0\le a<N.
 \tag{13}
\]
To prove this, put \(A=F_1\), \(B=K_1^{-1}F_{\rm r}\).
The actual weight relation gives \(AB=Q^{-1}BA\).
Induction therefore yields
\[
 (A+B)^a=\sum_{j=0}^a
       \frac{f_a}{f_jf_{a-j}}A^{a-j}B^j,\qquad a<N.
 \tag{14}
\]
Applied to \(w_0\otimes v\), its \(j\)-term divided by \(f_a\)
is \(x_1^{-j}w_{a-j}\otimes F_{\rm r}^jv/f_j\), which is (11).
The diagonal term is the identity and all other terms lower the
first-head occupation. Every term preserves total integer occupation,
so
\[
                              [S,K_\Sigma]=0.
 \tag{15}
\]
This is an actual finite change of source coordinates. It is not
declared to be an intertwining braid or a scalar-clock substitution.

At the quantum root, \(F_\Sigma^N=0\). Indeed the intermediate
Gaussian coefficients \({N\choose j}_Q\), \(0<j<N\), vanish,
while \(F_1^N=0\) and, by induction on the number of heads,
\((K_1^{-1}F_{\rm r})^N=0\). This uses primitivity of \(Q\),
not primality or oddness of \(N\).

Before root specialization the exact identity is instead
\[
 S^{-1}F_\Sigma S=F_1+J_N,\qquad
 J_N=\frac1{f_d}S^{-1}F_\Sigma^N(T_{0d}\otimes I),
 \quad T_{ab}=|a\rangle\langle b|.
 \tag{16}
\]
For \(a<d\), apply (13) on both sides of \(F_\Sigma S-SF_1\).
For \(a=d\) the difference is
\(F_\Sigma^N(w_0\otimes v)/f_d\). This proves (16) on every
column. Thus \(J_N=0\) at the root but all its normal derivatives
remain. Restricting later to the ordinary head path does not
justify deleting this tensor-prefix term.

## 3. Partial inverse and the two retained endpoint projectors

Define the finite one-head operator
\[
 L_Fw_a=(1-Q^a)^{-1}w_{a-1}\quad(a>0),\qquad L_Fw_0=0.
 \tag{17}
\]
It has
\[
                   F_1L_F=I-P_0,\qquad L_FF_1=I-P_d,
 \quad P_a=T_{aa}\otimes I.
 \tag{18}
\]
All denominators are among the actual units (5).
Set
\[
 C^\dagger=K_\Sigma^{-1}SL_FS^{-1},\qquad
 P_a^S=SP_aS^{-1}.
 \tag{19}
\]
At the root, (15)--(18) prove exactly
\[
                 CC^\dagger=I-P_0^S,\qquad
                 C^\dagger C=I-P_d^S.
 \tag{20}
\]
The defects have rank \(N^{m-1}\). In particular \(C^\dagger\)
is not an inverse of \(C\). The nilpotent \(C\) cannot acquire
a two-sided inverse under any finite Fourier similarity.

The endpoint coupons themselves are explicit. Since \(SP_0=P_0\)
and \(P_dS^{-1}=P_d\), (11)--(12) give
\[
 \begin{aligned}
 P_0^S&=P_0+\sum_{j=1}^d
   \frac{(-1)^jQ^{j(j-1)/2}x_1^{-j}}{f_j}
                   T_{0j}\otimes F_{\rm r}^j,\\
 P_d^S&=P_d+\sum_{j=1}^d
   \frac{x_1^{-j}}{f_j}T_{d-j,d}\otimes F_{\rm r}^j .
 \end{aligned}
 \tag{20a}
\]
They have total degree zero. Thus the difference from the original
highest or lowest probe is a specified sum of coupled source
insertions, not an unspecified boundary class.

There is a useful complete normal version. Since
\((T_{0d}\otimes I)L_F=0\), one has \(J_NL_F=0\).
Consequently (20) becomes, before specialization,
\[
 CC^\dagger=I-P_0^S,\qquad
 C^\dagger C=I-P_d^S+\mathcal R_N,
 \tag{21}
\]
\[
             \mathcal R_N=
                K_\Sigma^{-1}S L_FJ_NS^{-1}K_\Sigma.
 \tag{22}
\]
The whole row \(\mathcal R_N\), not only its zero root value,
belongs to the source-normal identity.

## 4. A finite Fourier clock with its full carry

The diagonal operator
\[
 G(w_a\otimes v)
  =f_a x_1^a Q^{-a(a-1)/2}\,w_a\otimes K_{\rm r}^{a}v
 \tag{23}
\]
is invertible on the same normal germ. Its consecutive ratio is
\((1-Q^{a+1})x_1Q^{-a}K_{\rm r}\). Hence
\[
                        G^{-1}(F_1K_\Sigma)G=U_1,
 \quad U_1w_a=w_{a+1}\ (a<d),\quad U_1w_d=0.
 \tag{24}
\]
This weights the complementary pivot itself, rather than only
\(F_\Sigma\), by a source-compatible diagonal gauge.

Choose an arbitrary nonzero evaluation radius \(\varrho\).
It is distinct from the residual geometric framing coordinate \(r\).
Put \(y_j=\varrho Q^j\) and
\[
 (V_\varrho)_{j,a}=N^{-1/2}y_j^a,\qquad
 (V_\varrho^{-1})_{a,j}
       =\sqrt N[X^a]\prod_{\ell\ne j}
                          \frac{X-y_\ell}{y_j-y_\ell}.
 \tag{25}
\]
The node differences are units at the primitive root.
This is the actual whole Vandermonde inverse, including away
from \(Q^N=1\). Define
\[
 Y=\operatorname{diag}(y_j),\quad
 u_N=N^{-1/2}(y_j^N)_j,\quad
 v^t=e_d^tV_\varrho^{-1},\quad
 \mathcal A=(V_\varrho G^{-1})S^{-1}.
 \tag{26}
\]
The identity on the other prefix heads is understood.
Evaluation of the missing last column of \(U_1\) gives
\[
                  V_\varrho U_1V_\varrho^{-1}=Y-u_Nv^t.
 \tag{27}
\]
Combining (16), (24) and (27) gives the full finite transition
\[
 \boxed{\quad
 \mathcal A C\mathcal A^{-1}=Y-u_Nv^t+\mathcal D_N,\qquad
 \mathcal D_N=V_\varrho G^{-1}J_NK_\Sigma G V_\varrho^{-1}.
 \quad}
 \tag{28}
\]
Neither the carry nor the normal term has been discarded.
The simultaneous Cartan operator is equally explicit. With
\(B_1=\operatorname{diag}(Q^a)\) and
\(\mathcal C_Q=V_\varrho B_1V_\varrho^{-1}\),
\[
 \mathcal A K_\Sigma\mathcal A^{-1}
       =x_1K_{\rm r}\mathcal C_Q^{-1},\qquad
 \mathcal A F_\Sigma\mathcal A^{-1}
       =(\mathcal A C\mathcal A^{-1})
                    (x_1K_{\rm r}\mathcal C_Q^{-1})^{-1}.
 \tag{28a}
\]
At the root \((\mathcal C_Qf)_j=f_{j+1}\), cyclically.
Off root its last row is the full interpolation row at
\(\varrho Q^N\). The entire transformed \(\mathcal E_\Sigma\)
and its prefix Casimir are retained as matrices; no scalar
Casimir channel is selected by (28a).
More explicitly define the whole ordered matrix
\[
 \Omega_\Sigma=F_\Sigma\mathcal E_\Sigma+
                       qK_\Sigma+q^{-1}K_\Sigma^{-1}.
 \tag{28b}
\]
The exact weight equation
\(K_\Sigma\mathcal E_\Sigma=Q\mathcal E_\Sigma K_\Sigma\)
gives, without an inverse of \(C\),
\[
 C\mathcal E_\Sigma
       =Q(\Omega_\Sigma K_\Sigma-qK_\Sigma^2-q^{-1}I),
 \tag{28c}
\]
\[
 \mathcal E_\Sigma
   =Q C^\dagger(\Omega_\Sigma K_\Sigma-qK_\Sigma^2-q^{-1}I)
                  +P_d^S\mathcal E_\Sigma-\mathcal R_N\mathcal E_\Sigma .
 \tag{28d}
\]
The last line follows from (21). It displays the additional
endpoint row and the generally nonscalar prefix Casimir needed
when transporting all three generators.

At the root there is a more explicit simultaneous formula before
the diagonal/Fourier steps. Write
\(\mathcal E_\Sigma=\mathcal E_1K_{\rm r}+\mathcal E_{\rm r}\)
with its original ordered coproduct on the remaining heads. Then
\[
 \begin{aligned}
 S^{-1}\mathcal E_\Sigma S(w_a\otimes v)
   ={}&w_a\otimes\mathcal E_{\rm r}v\\
     &+w_{a-1}\otimes
        (M_1K_{\rm r}Q^{-a}-M_1^{-1}K_{\rm r}^{-1})v
                                  \quad(a>0),
 \end{aligned}
 \tag{28e}
\]
and the second line is zero at \(a=0\).
To prove this, the zeroth column is fixed because \(S,S^{-1}\)
are the identity on \(w_0\otimes v\). The root head relations
and their ordered coproduct give
\[
 [S^{-1}\mathcal E_\Sigma S,F_1]
                  =\rho(K_\Sigma-K_\Sigma^{-1}),\qquad
 \rho=q-q^{-1}.
 \tag{28f}
\]
This determines each next column since \(1-Q^{a+1}\ne0\) for
\(a<d\). The lower coefficients in (28e) solve the recurrence
\[
 (1-Q^{a+1})b_{a+1}-(1-Q^a)b_a
       =\rho(x_1K_{\rm r}Q^{-a}-x_1^{-1}K_{\rm r}^{-1}Q^a).
 \tag{28g}
\]
This verifies (28e), including the forced endpoint convention.
Multiplication now gives the retained root Casimir matrix
\[
 S^{-1}\Omega_\Sigma S
     =F_1\otimes\mathcal E_{\rm r}
          -I\otimes(M_1K_{\rm r}+M_1^{-1}K_{\rm r}^{-1}).
 \tag{28h}
\]
In general it is not scalar. The formulas (28e)--(28h) are root
identities; their quantum normals must be taken from the whole
operators (16), (28b)--(28d), not by differentiating this
root simplification.

The root Fourier image is consequently explicit as well. Put
\(\mathcal T=\mathcal C_Q^{-1}\). Then
\[
 \boxed{\quad
 \mathcal A\mathcal E_\Sigma\mathcal A^{-1}
   =\mathcal T\mathcal E_{\rm r}
     +Y^{-1}x_1Q(\mathcal T-I)
              (M_1K_{\rm r}^2\mathcal T-M_1^{-1}I).
 \quad}
 \tag{28i}
\]
Indeed \(G^{-1}\mathcal E_{\rm r}G=Q^{-a}\mathcal E_{\rm r}\)
on the first occupation \(a\). Its lowering coefficient is
\(x_1Q(Q^{-a}-1)(M_1K_{\rm r}^2Q^{-a}-M_1^{-1})\).
The missing first-column correction in the Fourier transform of
\(L_1\) annihilates this coefficient exactly at \(a=0\).
This proves (28i), with the remaining-head operators and their
ordering unchanged. It inverts \(Y\), not the actual nilpotent
\(\mathcal A C\mathcal A^{-1}\).

At the root set \(\lambda=\varrho^N\) and
\(u_0=V_\varrho e_0=N^{-1/2}{\bf1}\). Then
\[
 u_N=\lambda u_0,\quad
 v_j=N^{-1/2}\varrho^{-d}Q^j,\quad
 \mathcal D_N=0,\qquad
 \mathcal A C\mathcal A^{-1}=Y-\lambda u_0v^t.
 \tag{29}
\]
Adding the omitted carry would replace the original unilateral
shift by \(U_1+\lambda T_{0d}\), whose \(N\)-th power is
\(\lambda I\). It changes the nilpotent central relation, so
this completion is not an equality of the original source.
For example the exact one-head determinant identities are
\[
 \det(tI-Y)=t^N-\lambda,\qquad
 \det(tI-Y+\lambda u_0v^t)=t^N.
 \tag{30}
\]
The carry's scalar resolvent coefficient is also explicit:
\[
                     v^t(tI-Y)^{-1}u_0=\frac1{t^N-\lambda}.
 \tag{31}
\]
Expand at large \(t\); root orthogonality keeps precisely the
powers \(t^{-N},t^{-2N},\ldots\), proving (31), hence its rational
continuation. This is a calibration of the universal carry,
not an evaluation against a knot-dependent source.

In the standard root metric the normalized Fourier matrix gives
\[
 \|V_\varrho\|\|V_\varrho^{-1}\|
       =\max(|\varrho|,|\varrho|^{-1})^d,\qquad
 \|\lambda u_0v^t\|=|\varrho|.
 \tag{32}
\]
Indeed \(\|u_0\|=1\), \(\|v\|=|\varrho|^{-d}\).
Thus small or large \(\varrho^N\) does not make the carry a small
operator: its norm equals that of \(Y\). No compact-central-radius
bound has been imported at a fixed nonunit \(\varrho\).

The exact root change between two evaluation radii is
\[
 (V_{\varrho'}V_\varrho^{-1})_{j,k}
   =\frac1N\sum_{a=0}^d
       (\varrho'/\varrho)^aQ^{(j-k)a}.
 \tag{33}
\]
Equivalently its numerator is
\(1-(\varrho'/\varrho)^N\), with the finite-sum removable values
retained. The upper endpoint is \(d\), not an infinite Fourier tail.

## 5. Original source, projectors and a finite endpoint current

Insert \(\mathcal A,\mathcal A^{-1}\) on the two sides of the
actual prefix interface. Every original matrix \(W\), source
vector, covector, pivot and occupation projector transforms by
that same map. For example \(W'=\mathcal A W\mathcal A^{-1}\)
and \(P'=\mathcal A P\mathcal A^{-1}\) satisfy
\[
                          \operatorname{Tr}(P'W')
                            =\operatorname{Tr}(PW).
 \tag{34}
\]
This applies to the literal highest or soft cut and arbitrary
marked defects. The projectors \(P_a^S\) in (20) are not reset
to the original \(P_a\). An occupation mask after the full
transition is the full conjugate of that mask.
Even on one head the Fourier kernel of an interval \(L\le a\le U\)
is
\[
             \frac1N\sum_{a=L}^UQ^{(j-k)a},
 \tag{35}
\]
with both endpoints. The \(S\)-conjugated coupled masks in (34)
must be retained before making any simplification like (35).

There is also an exact charge qualification. At the root the
Fourier carry pulled back to the original prefix is
\[
              \lambda S G(T_{0d}\otimes I)G^{-1}S^{-1}.
 \tag{35a}
\]
It has total integer degree \(1-N\). Its bare trace pairing with
a degree-zero unmarked word and diagonal cut/pivots is therefore
zero. Products or charged probes can supply compensating degree;
those actual coupons must remain. Nonzero rank of the carry
matrix alone is not a nonzero source period.

For a precise co-source identity put \(g=K_\Sigma^{1-N}\) and
\(\gamma=Q^{N-1}\). Since \(K_\Sigma C=Q^{-1}CK_\Sigma\),
\[
                                gC=\gamma Cg.
 \tag{36}
\]
For an arbitrary finite matrix \(B\), cyclicity and (21) give
\[
 \boxed{\begin{aligned}
 (1-\gamma)\operatorname{Tr}(gB)
   ={}&\operatorname{Tr}(gBP_0^S)
       -\gamma\operatorname{Tr}(gBP_d^S)\\
     &+\gamma\operatorname{Tr}(gB\mathcal R_N)
       +\operatorname{Tr}(g[B,C]C^\dagger).
 \end{aligned}}
 \tag{37}
\]
Indeed
\(\operatorname{Tr}(gBCC^\dagger)
 =\gamma\operatorname{Tr}(gBC^\dagger C)
   +\operatorname{Tr}(g[B,C]C^\dagger)\).
Substitute (21). Any original full functional
\(\operatorname{Tr}(P W)\) is covered by taking
\(B=g^{-1}P W\), with all original other pivots, cut factors
and scalar lines retained in that expression.

At the root \(\gamma=Q^{-1}\), \(\mathcal R_N=0\).
If in addition \([B,C]=0\), (37) reduces to the two-endpoint row.
The original marked source is not assumed to satisfy this
extra commutation. Equation (37) retains its actual defect.
It does not turn either endpoint functional into a known
nonzero scalar or supply a new multiplicative \(N\) normalization.

All these identities are formed on the whole fixed-\(N\) germ.
Differentiating a transformed matrix uses the forced connection
\[
 \partial_\alpha W'
   =\mathcal A(\partial_\alpha W)\mathcal A^{-1}
       +[(\partial_\alpha\mathcal A)\mathcal A^{-1},W'].
 \tag{38}
\]
The derivatives of \(S,G,V_\varrho,J_N,u_N,v\), the physical
two head walls and the prescribed source are all included.
If \(\varrho\) is parameter dependent, its derivatives are
included too. The ordinary head path is imposed on this whole
identity. It does not equate an ADO-pivot closed germ with the
ordinary Jones germ without their pivot and twist comparison.

## 6. What is proved at the geometric prefix zero

Equations (1)--(9) identify the exact classical complementary
entry, and (11)--(29) give a finite integer/source transition for
its ordered quantum lift. At a simple prefix zero the classical
unit \(c\) may be used as an analytic choice of evaluation radius
near a fixed Fourier label. This is a permitted parameter
substitution in an exact matrix identity, not a proof that
\(\mathcal A\) has a specified local stationary-phase amplitude.

In particular the invertible classical Bruhat chart (3) does not
justify inverting the nilpotent finite \(C\). Its exact substitute
is the partial inverse (20), or the diagonal Fourier clock together
with the carry and normal terms (28). The original source pairs
the carry through its transported coefficient
\(\lambda\operatorname{Tr}(P' u_0v^t W')\), with spectators and
ordering retained. That coefficient is not fixed by (31).

The quantum transform therefore supplies a relative chart and
explicit missing rows, rather than an unevaluated assertion that
all frames are equivalent. Its analytic matching to a regular
geometric generating function, the pairing of the carry with
the original source, and the resulting relative period remain
to be proved. No contributing cycle or scalar lower bound is
inferred from the classical regularity or finite invertibility
of the change of basis itself.

## Complete direct-source pins

* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* V: notes/actual_two_cut_fourier_polarization_and_cap.md, SHA256
  81edcc80bb8eae878e5c02f212d4110ea7faae37b3315b5fca877b291a3acc14.

The complete directs were read nontruncated in this active author
sequence, with unchanged complete reads explicitly retained where
applicable. The balanced full-Psi Fourier kernel, root holonomy
braiding and Weyl-gluing notes were also read completely for coverage:
their existing statements do not identify the present carry with
a geometric prefix-zero period. All proofs here use written
mathematics and text/hash operations only. No frozen or public
source file was edited.
