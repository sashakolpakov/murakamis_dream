# Shifted clocks and finite excursions in the actual bipyramid source

This note gives an exact reduction of the original full-minus-CROSS
numerator on the opposite-offset bipyramid. It retains the protected
face, the ordinary coefficient targets, the two middle positions of
every coupon, and all source phases. The main new reduction is a
nilpotent bad-state transfer and its finite Schur complement. It does
not prove the remaining exponential bound on that Schur complement.

Throughout, a high index means a middle **monomial exponent** greater
than \(\lfloor(N-1)/2\rfloor\), not a physical color. All derivative
identities are at the prescribed root. They are not generic-\(q\)
identities that can be differentiated in \(q\).

## 1. The exact source and its two kinds of indices

Let
\[
 N\ge2,\quad d=N-1,\quad h=\lfloor d/2\rfloor,\quad
 q=e^{\pi i/N},\quad
 s_r=2\sin(\pi r/N),\quad
 c_r=q^{2r+1}+q^{-2r-1}.
 \tag{1}
\]
The equator size \(m\ge6\) is even. Rim subscripts are taken modulo
\(m\). The north face is set to zero. The other protected face
\(z_0\) has target zero, equivalently it is set to zero after
forming the local polynomials. The south face is \(S\). The
remaining targets are
\[
 [S^d z_1^d\cdots z_{m-1}^d],\qquad t_0=0,\quad t_j=d\ (j\ne0).
 \tag{2}
\]
The polynomial statements are valid also at \(N=2\). Their application
to the published general-Morse physical source uses that exact
source identity in its stated range \(N\ge3\), with its original
component, cup, cap, and marked-cut normalization.
For an actual polynomial coupon \(p\), retain the root face operator
\[
 C(x,y)z^r
 =c_rz^r-s_r^2(x+y)z^{r-1}
                  -s_rs_{r-1}xy z^{r-2},
 \qquad
 H_p(x,b,c,y)=\sum_{r=0}^d[p(C_b)b^r]c^{d-r}.
 \tag{3}
\]
Terms with negative exponents vanish. The operator acts on
\(\mathbb C[b]/(b^N)\), with the full repeated-root functional
calculus. In particular, no derivative at a double spectral node is
discarded. For the full spectral numerator the coupon is
\[
 p(\Omega)=V_N(\sigma;\Omega)
 =\frac{\chi_N(\sigma)-\chi_N(\Omega)}{\sigma-\Omega},
 \qquad
 \chi_N(z)=2T_N(z/2)+2.
 \tag{4}
\]
Here \(T_N\) is the usual first-kind Chebyshev polynomial.
The quotient in (4) is a polynomial identity, including
\(\sigma=\Omega\). The same finite transport below applies to any
original fixed-power coupon reduced modulo \(\chi_N\).

The literal cyclic factors are
\[
 F_j=
 \begin{cases}
 H_{p_j}(0,z_{j-1},z_{j+1},z_j),&j\ \text{odd},\\
 H_{p_j}(S,z_{j+1},z_{j-1},z_j),&j\ \text{even}.
 \end{cases}
 \tag{5}
\]
The reversed middle order in the second row is part of the original
source, not a convention to be dropped. Write
\[
 F_j=\sum_{a,b,c}h_j(a,b,c;S)
                  z_{j-1}^{a}z_j^b z_{j+1}^c.
 \tag{6}
\]
For a north coupon, a nonzero coefficient has \(a+b+c=d\).
For a south coupon it is a scalar times
\(S^p\), where \(p=d-a-b-c\ge0\). In either case
\(a,c\ge0\) and \(a+c\le d\). The symbols \(a,c\) in (6)
are the two middle exponents, whereas \(b\) is the central
rim exponent, an outer position of (3).

The original matrix support says exactly
\[
       F_j^{\mathrm C}:\quad a\le h,\quad c\le h.
 \tag{7}
\]
Indeed an entry \(p(C)_{i,r}\) has middle powers
\(b^i c^{d-r}\). At even level, CROSS joins the lower half
to the upper half; at odd level it includes the central row
and column. Both cases give (7). Since \(2(h+1)>d\), a
non-CROSS coupon has exactly one high middle exponent.

Let \(\mathscr S\) and \(\mathscr S_{\mathrm C}\) denote (2)
applied to the products of \(F_j\) and \(F_j^{\mathrm C}\),
respectively. Our object is
\(\mathscr D=\mathscr S-\mathscr S_{\mathrm C}\).
These are the original scalar source coefficients. No absolute
values, reduced head count, or replacement face demands are used.

## 2. Literal transfer, including the unique marked jump

At the incoming state of row \(j\), use
\((u,v)\in\{0,\ldots,d\}^2\), and put
\[
 (T_j(S))_{(u,v),(u',v')}
 =h_j(t_{j-1}-u,\ u'-v,\ v';S).
 \tag{8}
\]
Every negative or unsupported exponent gives zero. For a nonzero
path, if \((a_j,b_j,c_j)\) is its local triple, then
\[
 u_j=c_{j-2}+b_{j-1},\qquad v_j=c_{j-1},
 \qquad
 a_{j+1}+b_j+c_{j-1}=t_j.
 \tag{9}
\]
These relations prove the exact, multiplicity-one correspondence
between cyclic transfer paths and original monomial selections.
Thus
\[
 \operatorname{tr}(T_0(S)\cdots T_{m-1}(S))
                         =S^d\mathscr S.
 \tag{10}
\]
The common \(S\) can therefore be set to \(1\) after forming the
literal transfer. It cannot be replaced by independent local
specializations. One direct check of (10) is
\[
 p_j=d-t_{j-1}+u_j+v_j-u_{j+1}-v_{j+1};
 \qquad \sum_j p_j=d.
 \tag{11}
\]
North rows have \(p_j=0\). All ordinary rows preserve or decrease
the grade \(u+v\); row \(j=1\) is the unique possible upward jump
by \(d\). This is the protected mark, not a periodic grading reset.

Let \(\mathcal V\) be the direct sum of the \(m\) state spaces,
with row \(j\) interpreted as the incoming state before \(T_j\).
Define the position-clock transfer \(L(S)\) by its only nonzero
blocks
\[
                L(S)_{j,j+1}=T_j(S).
 \tag{12}
\]
Block subscripts are cyclic. It follows that
\[
 \operatorname{tr}L(S)^m
      =mS^d\mathscr S,\qquad
 \mathscr S=-[z^m]\log\det(I-zL(1)).
 \tag{13}
\]
The second identity is formal at \(z=0\); it does not choose a
branch of a numerical logarithm.

## 3. CROSS becomes a diagonal state restriction

At incoming position \(j\), let \(P_j\) project onto
\[
             v\le h,\qquad 0\le t_{j-1}-u\le h.
 \tag{14}
\]
States with a negative \(t_{j-1}-u\) have zero outgoing row in
(8), so their arbitrary assignment would not change a cyclic
contraction. We use (14) to fix the definition. Put
\(P=\bigoplus_jP_j\), \(Q=I-P\).

The two inequalities in (14) are respectively
\(c_{j-1}\le h\) and \(a_j\le h\). Consequently
\[
 \operatorname{tr}(PL(S)P)^m=mS^d\mathscr S_{\mathrm C}.
 \tag{15}
\]
This is an exact equality of signed polynomials. It uses the
factorization of the local mask in (7), rather than treating a
projected coupon as another arbitrary polynomial in \(C\).
Away from the marked row, the good states are simply
\(u\ge d-h,\ v\le h\). At the marked row, \(u=0\) is required.

This choice of states is useful because every bad *internal*
interface of a nonzero path has a witness: either the preceding
coupon has high \(c\), or the following coupon has high \(a\).
A coupon can witness at most one interface.

## 4. The bad transfer is nilpotent, uniformly in the level

We prove the polynomial matrix identity
\[
                         (QL(S)Q)^{3m}=0.
 \tag{16}
\]
It is independent of the spectral parameters, the values of the
coupons, and \(N\).

First consider an aligned block of \(m+1\) consecutive nonzero
transitions, starting at row \(1\) and ending at the next row \(1\).
Its first north coupon has \(a_1=0\), since \(t_0=0\) in (8).
At the ending row \(1\), the same protected equation gives
\(c_{m-1}+b_0+a_1^{\mathrm{next}}=0\); all exponents are
nonnegative, so the last north coupon has \(c_{m-1}=0\).

The \(m/2\) north coupons between these endpoints have their
middle incidences on the even rim faces. A high middle incidence
cannot use the protected face \(z_0\). Each of the remaining
\(m/2-1\) even rim faces can receive at most one high incidence,
because two such incidences sum to more than its original target
\(d\); its additional outer incidence is nonnegative. Therefore
at least one of these north coupons is CROSS.

Now take an open nonzero path of \(3m\) transitions all of whose
states lie in \(Q\). There are \(3m-1\) internal bad interfaces.
Each needs a high incidence of one of the \(3m\) coupons, and a
coupon can supply at most one such incidence. Thus at most one
coupon along this path can be CROSS.

On the other hand, among any \(3m\) consecutive row indices
there are two consecutive aligned blocks of the preceding kind:
the first row \(1\) occurs within the first \(m\) transitions,
and the \(2m+1\) transitions from there through the second
following row \(1\) fit in the path. The two lists of \(m/2\)
north coupons are disjoint. Each list contains a CROSS coupon.
This contradicts the preceding upper bound of one, and proves
(16). The argument applies to the support of the matrix before
any signed cancellation.

In particular no all-bad directed cycle exists. This conclusion
is stronger than saying that the trace of one bad loop happens
to cancel. It also explains why the protected target cannot be
replaced by an ordinary periodic face target.

## 5. An exact finite-excursion formula for full-minus-CROSS

Decompose \(L=L(1)\) relative to \(P\mathcal V\oplus Q\mathcal V\):
\[
                 L=\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
 \tag{17}
\]
By (16), \(D^{3m}=0\), so
\[
 R_Q(z)=(I-zD)^{-1}=\sum_{r=0}^{3m-1}z^rD^r,\qquad
 K(z)=z^2B R_Q(z)C.
 \tag{18}
\]
The matrix \(K\) records an actual excursion from a good state
through one or more bad states and back to a good state.
All offsets, grades, original source coefficients, and their
signs are still in its entries.

The Schur complement gives
\[
 \begin{split}
 \det(I-zL)&=\det(I-zD)
          \det(I-zA-z^2B(I-zD)^{-1}C)\\
          &=\det(I-zA-K(z)).
 \end{split}
 \tag{19}
\]
Here \(\det(I-zD)=1\) follows from the proven nilpotence.
Combining (13),(15),(19) yields the closed formula
\[
 \boxed{\displaystyle
 \mathscr D
 =-[z^m]\log\det\!\left(I-(I-zA)^{-1}K(z)\right)
 =\sum_{\ell=1}^{\lfloor m/2\rfloor}
       \frac1\ell[z^m]\operatorname{tr}
       \left(((I-zA)^{-1}K(z))^\ell\right).}
 \tag{20}
\]
Everything is a formal finite coefficient calculation.
For the coefficient \(z^m\), only the terms of degree at most
\(m\) in the displayed resolvents are needed. Formula (20) is
not an expansion into absolute local sectors. It first retains
the signed sum inside each excursion and inside each good-state
propagator.

For a single coefficient \(z^m\), a formal Schur expansion would
truncate even without nilpotence. The additional theorem here is
the level-independent identity (16) for the entire bad transfer,
proved with the actual source mask and protected targets. The
Schur rewrite itself is a general algebraic identity, not an
analytic estimate.

The same identity may be written before setting \(S=1\), with
\([S^d]\) outside. Homogeneity (11) then removes that coefficient
only after the entire closed walk is formed. Thus the south
target has not disappeared from the derivation.

This formula isolates a concrete sufficient object for a source
bound: the finitely many signed excursion insertions in (20),
coupled to the original good-state transfer \(A\).
Neither nilpotence nor the polynomial dimension of these
matrices bounds their entries or their norms. An estimate on
those coupled terms at the original geometric rate is still
required.

## 6. Exact incidence clocks and the actual seam holonomy

The shifts in root integration by parts can be retained without
adding informal phase gauges. Multiply each local monomial in
row \(j\) by
\[
                q^{\alpha_j a+\beta_j b+\gamma_j c+\mu_jp}.
 \tag{21}
\]
Initially the exponents in (21) can be integers; they are then
periodic modulo \(2N\). They are independent *incidence* clocks,
not independent replacements of the physical face variables.
Using (8),(11), the modified transfer is exactly
\[
 \widetilde T_j
 =\kappa_j R_j^-\,T_j\,R_j^+,\qquad
 \kappa_j=q^{\alpha_jt_{j-1}+\mu_j(d-t_{j-1})},
 \tag{22}
\]
where the two diagonal matrices are
\[
 \begin{split}
 R_j^-(u,v)&=q^{(\mu_j-\alpha_j)u+(\mu_j-\beta_j)v},\\
 R_j^+(u,v)&=q^{(\beta_j-\mu_j)u+(\gamma_j-\mu_j)v}.
 \end{split}
 \tag{23}
\]
In a sewn product the intervening diagonal holonomy is therefore
\[
 \begin{split}
 R_{j-1}^+R_j^-(u,v)
 =q^{(\beta_{j-1}-\mu_{j-1}+\mu_j-\alpha_j)u}
  q^{(\gamma_{j-1}-\mu_{j-1}+\mu_j-\beta_j)v}.
 \end{split}
 \tag{24}
\]
This is a closed finite clock system on the original transfer
states. The good/bad projections commute with every matrix
in (23), so the same holonomies are retained in the excursion
formula, not discarded at its endpoints.

For a genuine common face shift \(z_j\mapsto q^{\lambda_j}z_j\)
and \(S\mapsto q^\mu S\), the incidence clocks satisfy
\[
 \alpha_j=\lambda_{j-1},\quad \beta_j=\lambda_j,\quad
 \gamma_j=\lambda_{j+1},\quad \mu_j=\mu.
 \tag{25}
\]
Then (24) is the identity and the remaining scalar is exactly
\[
              \prod_j\kappa_j
                =q^{d(\mu+\sum_{j=1}^{m-1}\lambda_j)}.
 \tag{26}
\]
This is precisely the original coefficient target (2).
Relative shifts of only some incident factors generally do
not satisfy (25). Their nontrivial matrices (24) are the
reason the shifted Ward current cannot be replaced by the
old unshifted current.

## 7. Root Ward identities close only with shifted targets

For clarity, the root operators in one ordinary face are
\[
 D_fP=\frac{P(qz_f)-P(q^{-1}z_f)}{iz_f},\quad
 T_fP=P(qz_f),\quad
 C_f=c_0-D_f(Z_f+x)(Z_f+y)D_f.
 \tag{27}
\]
On the quotient by \(z_f^N\), the top coefficient pairing
satisfies \(D_f^*=D_f\), but its product rule is
\[
 D_f(PQ)=(D_fP)(T_fQ)+(T_f^{-1}P)(D_fQ).
 \tag{28}
\]
In particular \([z_f^d]D_fP=0\), whereas the analogous
assertion at the protected target zero is false.

Let \(Z_{\mathbf t}(\boldsymbol\eta)\) be the original product
of coupons with incidence clocks, extracted at the explicitly
specified target \(\mathbf t\). For a derivative of one factor
at one incidence, the exact reduction is
\[
 [\mathbf z^{\mathbf t}]
      (D_f^{(j)}F_j)\prod_{k\ne j}F_k
 =\frac1i\left(
 Z_{\mathbf t+\mathbf e_f}(\boldsymbol\eta^{\,jf,+})
 -Z_{\mathbf t+\mathbf e_f}(\boldsymbol\eta^{\,jf,-})\right).
 \tag{29}
\]
Here \(\boldsymbol\eta^{\,jf,\pm}\) multiplies the existing
clock \(\eta_{jf}\) by \(q^{\pm1}\) and leaves every other
clock unchanged; it does not reset that clock to \(q^{\pm1}\).
The factor on the left is understood with the same existing
incidence clocks. A \(k\)-fold derivative has the corresponding clock
multiplier
\[
 \prod_{r=0}^{k-1}
       \frac{q^{-r}\mathcal T_{jf}
                    -q^{r}\mathcal T_{jf}^{-1}}{i}
 \quad\text{at target }\mathbf t+k\mathbf e_f,
 \tag{30}
\]
where \(\mathcal T_{jf}\) shifts only that incidence by \(q\).
Multiplication by a face monomial shifts the target in the
opposite direction. Equations (29),(30) follow coefficient
by coefficient from \(D_f^kz^a=\prod_{r=0}^{k-1}s_{a-r}z^{a-k}\).

Iterating (28) in the original factor order gives
\[
 \sum_j [\mathbf z^{\mathbf t}]
       \left(\prod_{k<j}T_f^{-1}F_k\right)
       (D_fF_j)
       \left(\prod_{k>j}T_fF_k\right)=0
       \qquad(t_f=d).
 \tag{31}
\]
Factors not incident to the face are unchanged. This finite
system can be represented entirely by the clocks (22)--(24)
and the shifted target family (29),(30). There are finitely
many targets: each local factor has degree \(d\), targets
outside the nonnegative total support are zero, derivatives
of order \(N\) of a local incidence vanish, and clocks have
period \(2N\).

There is one state-space qualification. For general shifted rim
targets, the partial load \(u=c_{j-2}+b_{j-1}\) can exceed \(d\).
To represent these auxiliary \(Z_{\mathbf t}\) by transfer, use
\(0\le u\le2d,\ 0\le v\le d\), the shifted target in (8),
and retain the requested coefficient of the common \(S\).
Alternatively, use their defining coefficient extraction directly.
The original smaller state space suffices only for the original
targets because then \(u\le t_{j-1}\le d\).

This is algebraic closure, not uniqueness or a norm bound
for Ward equations alone. In particular the good/bad
nilpotence proof in §4 uses the *original* targets. A shifted
target that can accommodate two high incidences must not be
treated as if it still had capacity \(d\). At even level,
raising an ordinary target from \(d=2h+1\) to \(d+1\) already
changes that capacity. The exact target shifts in (29) are
therefore essential.

The finite resolvent construction (3),(4),(8),(20) supplies
the actual solution of these identities. It retains the
finite spectral endpoints and normal data even when
spectral values coincide. Differentiation in \(\sigma\) of
the resulting polynomial identities is legitimate;
differentiation of the fixed-\(N\) root quotient identities
in \(q\) is not.

## 8. A sign holonomy and a noncancelling corner

There is also a useful exact sign version of the clock
description for the full numerator. Fix real
\(\sigma<c_0\), away from the nodes, and set
\[
 b_r=\operatorname{sgn}(\sigma-c_r),\qquad
 \epsilon_i=(-1)^i\prod_{r<i}b_r.
 \tag{32}
\]
Every nonzero coefficient of an entry \(V_N(\sigma;C(x,y))_{i,j}\)
has sign
\[
                   (-1)^d\epsilon_i\epsilon_{d-j}.
 \tag{33}
\]
Here is a direct proof retaining the unused factors. The
division-free path numerator \(P_{i,j}\) satisfies
\[
 P_{i,i}=1,\quad
 P_{i,j}=-s_j^2(x+y)P_{i,j-1}
        -s_js_{j-1}xy(\sigma-c_{j-1})P_{i,j-2}.
 \tag{34}
\]
With \(x=S,y=1\), divide it by
\((-1)^{j-i}\prod_{r=i+1}^j s_r^2\).
The normalized polynomial \(H_k\), \(k=j-i\), has
\[
 H_0=1,\quad H_1=1+S,\qquad
 H_k=(1+S)H_{k-1}-SH_{k-2}
       +\frac{c_0-\sigma}{s_{i+k}s_{i+k-1}}SH_{k-2}.
 \tag{35}
\]
For \(F_k=1+\cdots+S^k\), the exact free recurrence gives
\[
 H_k=F_k+\sum_{r=2}^k
   \frac{c_0-\sigma}{s_{i+r}s_{i+r-1}}
                 S F_{k-r}H_{r-2}.
 \tag{36}
\]
Its coefficients are positive. Homogenization recovers all
outer splits. Multiplying the unused prefix
\(\prod_{r<i}(\sigma-c_r)\) and suffix
\(\prod_{r>j}(\sigma-c_r)\), and using \(c_{d-r}=c_r\),
proves (33).

Consequently the literal transfer factors as a nonnegative
matrix with diagonal signs on each side. At an incoming
interface \(j\), the resulting sewn sign is exactly
\[
                 \epsilon^{(j-1)}_v
                    \epsilon^{(j)}_{t_{j-1}-u}.
 \tag{37}
\]
The common local factor \((-1)^d\) contributes \(1\)
around the even \(m\)-cycle. Formula (37) preserves the
independent spectra and the original grade, and is not a
claim that the signs cancel. Any diagonal sign on the
finite state space can equivalently be expanded in the
finite root clocks.
When it is written as a full diagonal matrix, values of
\(\epsilon_{t_{j-1}-u}\) at unsupported negative indices
may be set arbitrarily to \(1\); the corresponding outgoing
rows vanish.

At even level and \(\sigma_j=-2\) for every \(j\), all
\(\epsilon_i=1\). Every local coefficient has sign
\((-1)^d=-1\); hence every sewn product has positive sign.
Full-minus-CROSS is then a nonnegative complementary sum.
It is nonzero at every even level. For example select the
pure outer monomial \(S^d\) in box \(0\), the pure outer
monomial \(z_j^d\) in every other box except \(2,3\),
and the middle monomials \(z_3^d,z_2^d\) in boxes \(2,3\).
These have exactly the targets (2). Both exceptional
coupons are non-CROSS. Each pure outer coefficient is
\((-1)^d\prod_{r=1}^d s_r^2=-N^2\), and each selected
middle diagonal coefficient is
\[
 \frac{\chi_N(-2)}{-2-c_0}
     =-\sec^2\!\left(\frac{\pi}{2N}\right).
 \tag{38}
\]
Thus this one actual contribution gives
\[
 \mathscr D(-2,\ldots,-2)
       \ \ge\ (N^2)^{m-2}
                    \sec^4\!\left(\frac{\pi}{2N}\right)>0
       \qquad(N\ \text{even}).
 \tag{39}
\]
This polynomial lower witness does not refute an exponential
gap below the geometric source rate. It does rule out an
argument that seeks that gap solely by cancellation at
every spectral point.

## 9. The general middle-incidence obstruction

There is a useful graph formulation that does not depend on
this bipyramid. In an original matched quadrilateral source,
make a bipartite incidence graph with one left vertex for
each coupon and one right vertex for each ordinary middle
face. Connect a coupon to its two middle faces, deleting
protected faces whose target is zero. A non-CROSS coupon
must assign its unique high middle exponent to one of
these neighbors. Since two high incidences exceed an
ordinary target \(d\), different such coupons must use
different neighbors.

It follows directly, without a matching theorem, that for
every set \(E_0\) of coupons,
\[
 \#\{\text{CROSS coupons in }E_0\}
                  \ge |E_0|-|\mathcal N_{\mathrm{ord}}(E_0)|.
 \tag{40}
\]
The right side can be negative, in which case the statement
is vacuous. Protected faces, actual middle positions, and
ordinary target capacities are part of (40).
For the bipyramid north coupons the right side is one.
This is a necessary support restriction; it is not a
sufficient description of the full source or a statement
about every assignment with at least one non-CROSS coupon.

For a matched triangulated sphere with \(R\) coupons, the
middle-incidence multigraph has \(R\) edges on \(R+2\)
white vertices, including isolated vertices, and two
protected vertices. There is an injection of every edge
to an ordinary endpoint if and only if each connected
component is either a tree containing exactly one
protected vertex, or a unicyclic component containing
neither protected vertex. To prove necessity, a component
with \(E_C\) edges, \(V_C\) vertices, and \(p_C\) protected
vertices has \(E_C\le V_C-p_C\). The sums of the two sides
are both \(R\), so equality holds in every component.
Connectedness gives \(E_C\ge V_C-1\), whence \(p_C\le1\)
and the stated two possibilities. Conversely, orient each
tree away from its protected root, and orient each unique
cycle cyclically with its attached trees away from the
cycle. Assign an edge to its head. This gives the desired
injection, also for multiple edges. This characterizes
absence of the all-high incidence obstruction only;
the remaining monomial degrees and original targets
can impose further restrictions.

If another literal finite transfer realizes the original
targets and has a repeated deficient coupon block, the same
open-path counting method can be used there. Constructing
such a transfer with its actual Morse heads and marked
targets is a separate requirement. No general sphere
transfer or analytic gap follows from (40) alone.

## 10. What has and has not been reduced

The full sewn difference is now an exact finite-excursion
coefficient (20), with a bad resolvent of length bounded
independently of the level. The relative face shifts are
the explicit finite seam holonomies (24); actual common
face shifts reduce to the correct target scalar (26).
The root Ward identities close on those clocks only when
their shifted coefficient targets are retained.

The older unshifted Green-current cancellation is false
and is not used. Nor is there a claim that every
non-CROSS sector requires several spectral perturbations:
the exact odd-level one-exception counterexample survives.
The remaining analytic problem is to bound the signed,
fully coupled terms in (20) at the original geometric
rate. Nilpotence supplies a finite list of excursion
types; it does not supply their exponential size.

## 11. Bounded exact reproduction

The standalone standard-library runner
md-shifted-cyclic-excursion-audit.py constructs the local
numerators by powers of the original matrix (3), checks
their full polynomial resolvent equation, and compares
direct homogeneous monomial extraction with the transfer
and Schur formulas. Its recorded scope is:

* sixteen exact finite-field cases, \(N=2,3,4,5\),
  \(m=6\), using two fields and two spectral tuples per
  level; both FULL and CROSS coefficients and (20) are
  checked;
* ninety-six incidence-clock checks of (22),(23);
* ten homogeneous support graphs, \(N=2,\ldots,6\),
  \(m=6,8\), checked for acyclicity and longest bad path
  below \(3m\);
* two shifted-target checks that agree with direct
  extraction only after enlarging \(u\) to \(2d\);
* exact integer recovery of the \(N=3\) nonzero sewn
  current and the one-exception full-minus-CROSS
  counterexample.

The output is md-shifted-cyclic-excursion-results.json.
These are finite identity checks, separate from the
all-level support proof in §4. They assert neither a
uniform spectral estimate nor an asymptotic gap.

