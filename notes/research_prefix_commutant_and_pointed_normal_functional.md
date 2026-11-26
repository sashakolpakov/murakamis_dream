# Prefix commutants and the original pointed normal functional

Private written proof, 18 November 2026.

The actual total-prefix change of coordinates reduces an intertwiner
to a polynomial in one nilpotent raising operator. The remaining
lowering equation is an explicit finite recursion. The original
highest-cut, pivotal source retains every coefficient of that
polynomial; it does not in general factor through its constant
coefficient at the complete root.

There is nevertheless a constructive reduction through the **whole
meridian germ** of that constant coefficient. It is a universal
meromorphic trace functional whose value on an actual analytic
intertwiner is removable. Its pole order is at most \(N-1\), so a
meridian jet of order at most \(N-1\) suffices. No minimal-depth or
uniform norm assertion is made.

A universal two-head Casimir coupon detects the distinction. Its
constant coefficient vanishes at the root, whereas its original
pivotal partial trace is \(N I\). It is square-zero, and adding any
multiple of it to the identity gives an invertible intertwiner with
the same constant coefficient and a varying pointed source. This
is an obstruction inside the actual intertwiner/coupon algebra,
not a counterexample about a knot or the image of the braid group.

The complete directs are P, the actual relative prefix transition,
and M, the original pivotal and cut conventions. All additional
algebra and source evaluations are proved below.

## 1. The exact root commutant

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
The quantum parameter stays fixed in Sections 1--5. Meridian
parameters remain unspecialized near their complete values.
On each actual balanced head,
\[
 K_iw_a=x_iQ^{-a}w_a,\qquad x_i=-M_i/q,
 \quad F_iw_a=(1-Q^{a+1})w_{a+1}\quad(a<d),
 \tag{1}
\]
with \(F_iw_d=0\), and
\[
 \mathcal E_iw_a=(M_iQ^{-a}-M_i^{-1})w_{a-1}\quad(a>0),
 \qquad \mathcal E_iw_0=0.
 \tag{2}
\]
Put \(f_a=\prod_{j=1}^a(1-Q^j)\), \(f_0=1\); all \(f_a\),
\(a<N\), are units.

Split a total prefix of \(m\) heads into its first head and its
remaining ordered tensor product. Write \(K_{\rm r},F_{\rm r},
\mathcal E_{\rm r}\) for the actual remaining coproducts. For
\(m=1\), use \(K_{\rm r}=I\) and \(F_{\rm r}=\mathcal E_{\rm r}=0\).
P gives the exact finite operator
\[
 S=\sum_{j=0}^{d}\frac{(x_1^{-1}L_1F_{\rm r})^j}{f_j},
 \qquad L_1w_a=w_{a-1},\quad L_1w_0=0,
 \tag{3}
\]
with its finite inverse and original source transport. At the root,
\[
 S^{-1}F_\Sigma S=F_1,\qquad [S,K_\Sigma]=0,
 \quad K_\Sigma=K_1K_{\rm r}.
 \tag{4}
\]
The transformed lowering operator is
\[
 E':=S^{-1}\mathcal E_\Sigma S
       =I\otimes\mathcal E_{\rm r}+L_1b_A,\qquad
 b_a=M_1K_{\rm r}Q^{-a}-M_1^{-1}K_{\rm r}^{-1}.
 \tag{5}
\]
Here \(b_A\) is evaluated at the input first-head occupation \(a\);
the second term is zero at \(a=0\).

Let \(W\) be an endomorphism commuting with the actual total
\(F_\Sigma,K_\Sigma,\mathcal E_\Sigma\). This includes an unmarked
actual braid endomorphism with its colors matched at the two ends.
It does not include arbitrary inserted marks without their Ward
commutators. Define \(W'=S^{-1}WS\).

Since \(F_1\) is one Jordan block with nonzero arrows below its
last row, its full matrix commutant on the tensor product is
\[
                  W'=\sum_{n=0}^{d}F_1^n\otimes B_n.
 \tag{6}
\]
For an elementary proof, define \(B_n\) by
\[
 W'(w_0\otimes v)=\sum_{n=0}^{d}f_nw_n\otimes B_nv.
 \tag{7}
\]
Commutation with \(F_1\) determines every other column from (7),
giving (6) uniquely. Commutation with \(K_\Sigma\) is equivalent to
\[
                        K_{\rm r}B_n=Q^nB_nK_{\rm r}.
 \tag{8}
\]
If \(W\) preserves total integer occupation, as the unmarked
literal braid does, \(B_n\) has integer occupation degree \(-n\)
on the remaining heads. Equation (8) alone only records its
root weight.

Set
\[
                       D=M_1K_{\rm r}+M_1^{-1}K_{\rm r}^{-1}.
 \tag{9}
\]
The full remaining lowering condition is exactly
\[
 \boxed{\quad
 [\mathcal E_{\rm r},B_{n-1}]
    =-(1-Q^n)b_nB_n=[D,B_n]\quad(1\le n\le d),
 \qquad [\mathcal E_{\rm r},B_d]=0.
 \quad}
 \tag{10}
\]
Indeed the first-head \(w_{n-1}\) coefficient of
\([E',W'](w_0\otimes v)\), divided by \(f_{n-1}\), is
\[
 [\mathcal E_{\rm r},B_{n-1}]+(1-Q^n)b_nB_n.
 \tag{11}
\]
The last coefficient is \(f_d[\mathcal E_{\rm r},B_d]\).
The second equality in (10) follows from (8).
These conditions are sufficient too: the root relation
\([E',F_1]=(q-q^{-1})(K_\Sigma-K_\Sigma^{-1})\) and
\([W',K_\Sigma]=[W',F_1]=0\) imply that \([E',W']\) commutes
with \(F_1\). Its vanishing on \(w_0\otimes v\) then gives
its vanishing on every column.

The last equation of (10) is a genuine closing condition. It
cannot be omitted by working only with the transformed Casimir.

## 2. The original pointed and pivotal source

Write \(g_{\rm r}=K_{\rm r}^{\,1-N}\). In M's original braid
closure convention the highest-cut source, before any additional
unchanged scalar framing or peripheral line, is
\[
 \Phi_0(W)=
  \operatorname{Tr}\bigl((P_0\otimes g_{\rm r})W\bigr).
 \tag{12}
\]
All literal crossing scalars can equivalently be included in \(W\).
No new pivot is inserted on the opened head.

The original source in (12) is not its reset value in the \(S\)
coordinates. Its exact expression is
\[
 \boxed{\quad
 \Phi_0(W)=
   \operatorname{Tr}_{\rm r}\left(
      g_{\rm r}\sum_{n=0}^{d}x_1^{-n}F_{\rm r}^{\,n}B_n
                           \right).
 \quad}
 \tag{13}
\]
To prove it, \(S^{-1}(w_0\otimes v)=w_0\otimes v\).
Apply (7), then (3). Only the \(j=n\) term of \(S\) returns
the first head to zero. Its coefficient is
\(x_1^{-n}F_{\rm r}^n/f_n\), cancelling the \(f_n\) in (7).
The remaining trace is exactly (13), in the displayed order.

For any other prescribed cut probe \(P\), the always valid source
formula is instead
\[
 \Phi_P(W)=
 \operatorname{Tr}\left[
   S^{-1}(P\otimes g_{\rm r})S
       \sum_{n=0}^{d}F_1^n\otimes B_n\right].
 \tag{14}
\]
This includes the original soft diagonal probes. If the actual
unmarked cut operator is scalar, M's exact source identity makes
all trace-one probes equal; it does not authorize replacing the
transformed probe in (14) by an untransformed one. Arbitrary
marked words retain their nonzero Ward defects and are not
silently put in the homogeneous commutant (6).

## 3. A nonzero source class in the kernel of the root constant term

Take two actual complete heads, so \(M_1=M_2=1\),
\(x_1=x_2=x=-q^{-1}\), and \(x^2=Q^{-1}\).
In (6) take
\[
 B_0=\cdots=B_{d-1}=0,\qquad B_d=T_{0d}=|0\rangle\langle d|.
 \tag{15}
\]
Equation (8) holds since \(K_2T_{0d}=Q^dT_{0d}K_2\).
Both \(\mathcal E_2T_{0d}\) and \(T_{0d}\mathcal E_2\) vanish.
The only other condition in (10) is
\[
 b_dT_{0d}=(xQ^{-d}-x^{-1})T_{0d}
                 =(Qx-x^{-1})T_{0d}=0.
 \tag{16}
\]
Thus
\[
             R_N=S(F_1^d\otimes T_{0d})S^{-1}
 \tag{17}
\]
is an actual total-degree-zero intertwiner, not just a matrix
commuting with one generator.

The whole retained source is computable. At the root,
\[
 f_d=N,\qquad
 f_{d-a}=\frac{N(-1)^aQ^{a(a+1)/2}}{f_a}.
 \tag{18}
\]
The first identity follows by evaluating
\((t^N-1)/(t-1)=\prod_{j=1}^{d}(t-Q^j)\) at \(t=1\).
To obtain the second, separate the last \(a\)
factors of \(f_d\), use
\(1-Q^{-j}=-Q^{-j}(1-Q^j)\), and solve for \(f_{d-a}\).
Using (3) and its finite inverse from P gives
\[
 R_N=N|\psi\rangle\langle\phi|,\qquad
 |\psi\rangle=\sum_{a=0}^{d}x^{a-d}|a,d-a\rangle,\quad
 \langle\phi|=\sum_{a=0}^{d}x^{-a}Q^{-a}\langle a,d-a|.
 \tag{19}
\]
For example the coefficient of \(\langle a,d-a|\) in
\(\langle0,d|S^{-1}\) is
\((-1)^aQ^{a(a-1)/2}x^{-a}N/(f_af_{d-a})=x^{-a}Q^{-a}\).
These are bilinear algebraic vectors and covectors, with no
complex conjugation.

Their pairing is \(x^{-d}\sum_aQ^{-a}=0\), so
\[
                              R_N^2=0.
 \tag{20}
\]
Nevertheless its original pivotal partial trace is
\[
 \boxed{\quad
 \operatorname{Tr}_2\bigl((I\otimes K_2^{1-N})R_N\bigr)=N I.
 \quad}
 \tag{21}
\]
Indeed the support in (19) makes the partial trace diagonal.
On its \(a\)-th diagonal the factor is
\[
 N x^{-d}Q^{-a}\cdot x^{-d}Q^{a+1}
       =N x^{-2d}Q=N.
 \tag{22}
\]
In particular \(\Phi_0(R_N)=N\), and every trace-one cut probe
has the same value. Any fixed external scalar line multiplies
this value unchanged; (21) is not an additional normalization
factor for a knot invariant.

The map from the commutant to its constant coefficient \(B_0\)
is an algebra homomorphism. Its kernel is nilpotent of order at
most \(N\), by positive \(F_1\)-degree. In particular
\[
 I+tR_N\text{ is invertible for every }t,\qquad
 B_0(I+tR_N)=I,\qquad \Phi_0(I+tR_N)=tN.
 \tag{23}
\]
Here \(\Phi_0(I)=x^{-d}\sum_aQ^{-a}=0\).
Thus neither the root value \(B_0\) nor that value together with
invertibility determines the prescribed source on the full
actual intertwiner algebra.

## 4. An actual Casimir lift of the kernel coupon

The coupon (17) extends through a whole root-quantum meridian
family. Use the actual total Casimir
\[
 \Omega_\Sigma=F_\Sigma\mathcal E_\Sigma+
                    qK_\Sigma+q^{-1}K_\Sigma^{-1}.
 \tag{24}
\]
The root head relations, including their endpoint rows, imply
that (24) commutes with all three total generators. This also
follows directly by expanding each commutator with
\([\mathcal E_\Sigma,F_\Sigma]=(q-q^{-1})
(K_\Sigma-K_\Sigma^{-1})\) and the two weight relations.

At the two-head complete point, P's exact formula reads
\[
 S^{-1}\Omega_\Sigma S=F_1\mathcal E_2+
                              \operatorname{diag}(\lambda_b),
 \quad \lambda_b=q^{2b+1}+q^{-(2b+1)},\quad 0\le b\le d.
 \tag{25}
\]
The diagonal in (25) is on the second head. Define the monic
degree-\(d\) polynomial
\[
                         p_N(t)=\prod_{b=1}^{d}(t-\lambda_b).
 \tag{26}
\]
The only coincidences of the \(\lambda_b\) are
\(\lambda_a=\lambda_b\) with \(a=b\) or \(a+b=d\).
Indeed \(z+z^{-1}=w+w^{-1}\) implies \(z=w\) or \(zw=1\);
apply this to \(z=qQ^a,w=qQ^b\).

On a fixed total-occupation subspace, (25) is bidiagonal with
tail index in a consecutive interval of \(0,\ldots,d\).
Every proper such interval has characteristic polynomial
dividing \(p_N\): the omitted occurrence \(\lambda_0\) is
duplicated by \(\lambda_d\), and a proper interval cannot
contain both endpoints. Cayley--Hamilton therefore kills
each proper interval block. The same argument kills every
entry of \(p_N\) on the full block except the longest
off-diagonal: a polynomial entry between two ordered indices
depends only on their intervening bidiagonal interval.
For the longest entry, only the leading degree-\(d\) term
can travel all \(d\) steps and its coefficient is one. Hence
\[
 p_N(S^{-1}\Omega_\Sigma S)
       =F_1^d\mathcal E_2^d
       =(-1)^dN(F_1^d\otimes T_{0d}),
 \tag{27}
\]
because
\(\prod_{a=1}^{d}(Q^{-a}-1)=Q^{-d(d+1)/2}f_d=(-1)^dN\).
Consequently
\[
                         R_N=\frac{p_N(\Omega_\Sigma)}{(-1)^dN}.
 \tag{28}
\]

Keep \(q=q_N\) fixed and let the two meridians vary together
near \(M=1\). The same polynomial of the actual matrix
\(\Omega_\Sigma(M)\), with the coefficients (26) fixed, is an
analytic intertwiner family specializing to (17). Its constant
coefficient vanishes at \(M=1\), while its source does not.
For each fixed \(t\), \(I+tR_N(M)\) is invertible on a sufficiently
small meridian disk. Thus (23) is compatible with actual
meridian-analytic coupons, not only with an isolated root fiber.

No assertion that (28) is a literal braid word is needed or made.
The conclusion is precisely that the homogeneous Ward equations
and invertibility alone cannot give the proposed value-only
source factorization. A stronger restriction on the image of
actual knot words would be an additional input.

## 5. Constructive reconstruction from the whole meridian germ

Return to \(m\) heads and vary their common meridian \(M\), still
at fixed \(q_N\). Let \(W(M)\) be an analytic family of actual
total intertwiners. All matrices in (3)--(10) are analytic near
\(M=1\). Each \(b_n(M)\) is diagonal on the remaining-head
occupation basis. If their total occupation is \(A_{\rm r}\),
its diagonal entry is
\[
 (-q^{-1})^{m-1}M^mQ^{-A_{\rm r}-n}
       -(-q)^{m-1}M^{-m}Q^{A_{\rm r}}.
 \tag{29}
\]
It is not identically zero. Every zero at \(M=1\) is simple:
the derivative there is \(2m\) times its first nonzero summand.
There are only finitely many other zeros for fixed \(N,m\).
Choose a punctured meridian disk excluding them. Then (10)
recovers every coefficient uniquely:
\[
 B_n=\mathscr D_n(B_{n-1}),\qquad
 \mathscr D_n(B)=
       -\frac{b_n^{-1}[\mathcal E_{\rm r},B]}{1-Q^n}.
 \tag{30}
\]
Its \(n\)-fold composition has pole order at most \(n\) at
\(M=1\). For an actual analytic intertwiner these apparent poles
cancel. The top condition \([\mathcal E_{\rm r},B_d]=0\), the
weight relations, and those cancellations remain restrictions
on admissible \(B_0\); an arbitrary analytic matrix is not
declared admissible.

There is an explicit reduced source functional as well. For the
ordinary matrix trace pairing, the adjoint of (30) is
\[
 \mathscr D_n^*(A)
      =\frac{[\mathcal E_{\rm r},A b_n^{-1}]}{1-Q^n},
 \qquad
 \operatorname{Tr}(A\mathscr D_n(B))
       =\operatorname{Tr}(\mathscr D_n^*(A)B).
 \tag{31}
\]
This follows by cyclically moving the single commutator; the
position of \(b_n^{-1}\) in (31) is essential. Define the known
meromorphic remaining-head matrix
\[
 \mathcal H_N(M)=
   \sum_{n=0}^{d}x_1^{-n}
      (\mathscr D_1^*\circ\cdots\circ\mathscr D_n^*)
                         (g_{\rm r}F_{\rm r}^{\,n}),
 \tag{32}
\]
with \(n=0\) term \(g_{\rm r}\). Equations (13), (30), and (31)
give exactly on the punctured disk
\[
                 \Phi_0(W(M))
                     =\operatorname{Tr}_{\rm r}
                           (\mathcal H_N(M)B_0(M)).
 \tag{33}
\]
The left side is the original analytic source, so (33) has its
prescribed removable continuation. The pole order of
\(\mathcal H_N\) is at most \(d\). Equivalently,
\[
 \Phi_0(W(1))=
 [t^0]\operatorname{Tr}_{\rm r}
          (\mathcal H_N(1+t)B_0(1+t)).
 \tag{34}
\]
Only the meridian jet of \(B_0\) through order at most \(d=N-1\)
can enter (34). This is an upper bound, not a proof that depth
\(N-1\) is necessary. Equations (17)--(28) only exclude depth
zero as a universal replacement. No bound uniform in \(N\)
for the coefficients of (34) is inferred.

## 6. An explicit scalar \(K\)-Casimir kernel

The matrix \(\mathcal H_N\) in (32) has a more explicit universal
form. Set \(K=K_{\rm r}\), \(F=F_{\rm r}\), \(E=\mathcal E_{\rm r}\),
and retain the actual remaining-head Casimir
\[
 \Omega=FE+qK+q^{-1}K^{-1},\qquad
 u(k,\omega)=\omega-qk-q^{-1}k^{-1}.
 \tag{35}
\]
It commutes with \(K,F,E\) by the same root relations used in
Section 4. No scalar Casimir value or simple spectrum is assumed.
For an empty remaining tensor use \(K=I,F=E=0\) and
\(\Omega=(q+q^{-1})I\).

For every \(0\le n\le d\) define scalar rational functions
\(a_{n,j}(k,\omega)\), \(0\le j\le n\), by
\[
 a_{n,n}(k,\omega)=Q^{-n}k^{1-N},\qquad
 b_j(k)=M_1kQ^{-j}-M_1^{-1}k^{-1},
 \tag{36}
\]
and, descending from \(j=n\) to \(1\), by
\[
 \boxed{\quad
 a_{n,j-1}(k,\omega)=\frac1{1-Q^j}
 \left[
   \frac{u(Q^{-j}k,\omega)a_{n,j}(k,\omega)}{b_j(k)}
   -\frac{u(k,\omega)a_{n,j}(Qk,\omega)}{b_j(Qk)}
 \right].
 \quad}
 \tag{37}
\]
Then the actual universal matrix in (32) is exactly
\[
 \mathcal H_N(M)=\mathfrak h_N(K,\Omega;M_1),\qquad
 \mathfrak h_N(k,\omega;M_1)
       =\sum_{n=0}^{d}x_1^{-n}a_{n,0}(k,\omega).
 \tag{38}
\]
This is rational in the nonzero \(k\) and meridian, and polynomial
of degree at most \(d\) in \(\omega\). Its evaluation uses the
commuting matrices \(K,\Omega\), retaining every Casimir Jordan
block.

Here is a direct verification of all shifts and orders. The exact
relations give \(FE=u(K,\Omega)\), \(EF=u(Q^{-1}K,\Omega)\),
\(f(K)F^r=F^rf(Q^{-r}K)\), and \(f(K)E=Ef(QK)\).
Consequently, for \(r\ge1\) and \(v=v(K,\Omega)\),
\[
 [E,F^rv]
   =F^{r-1}\{u(Q^{-r}K,\Omega)v(K,\Omega)
                    -u(K,\Omega)v(QK,\Omega)\}.
 \tag{39}
\]
Also \(g_{\rm r}F^n=F^nQ^{-n}K^{1-N}\), since \(Q^N=1\).
Apply (31) successively for \(j=n,n-1,\ldots,1\). In (39) put
\(r=j\) and \(v=a_{n,j}/b_j\). This gives (37) and then (38),
with precisely the adjoint order of (32).
Every step adds at most one degree in \(\omega\).
The denominators are only the displayed shifted \(b_j\)'s and
the nonzero constants \(1-Q^j\). Their meridian zeros remain
simple individually, so the pole bound in Section 5 is unchanged.

There is an exact scalar contour form if desired. On the common
meridian family put \(x_{\rm r}=(-M/q)^{m-1}\),
\(k_a=x_{\rm r}Q^{-a}\), and
\[
 \Pi_a=\frac1N\sum_{\ell=0}^{d}
               (Q^aK/x_{\rm r})^\ell,\qquad 0\le a<N.
 \tag{40}
\]
These are the actual root weight projectors, including zero
projectors for absent weights. They commute with \(\Omega\).
For fixed \(N\), choose a small meridian circle \(|t|=\epsilon\)
where all denominators are units, and a sufficiently large fixed
circle \(|\zeta|=R\) enclosing the spectra of \(\Omega(1+t)\)
for \(|t|\le\epsilon\). Polynomial functional calculus and (34)
give, in the original source normalization,
\[
 \begin{aligned}
 \Phi_0(W(1))
  =\frac1{(2\pi i)^2}
    \int_{|t|=\epsilon}\frac{dt}{t}
    \int_{|\zeta|=R}d\zeta\,
       \sum_{a=0}^{d}
       &\mathfrak h_N(k_a(1+t),\zeta;1+t)\\[-2pt]
       {}\cdot&
       \operatorname{Tr}_{\rm r}
       \left(\Pi_a(\zeta I-\Omega(1+t))^{-1}B_0(1+t)\right).
 \end{aligned}
 \tag{41}
\]
Both circles have positive orientation. There is no commutation
of \(B_0\) with \(\Omega\) in this formula. The resolvent retains
its full higher poles, and the meridian integral is the finite
part already fixed by the actual source. These auxiliary finite
contours do not assert a pushforward of a geometric framing
cycle or an asymptotic bound.

## 7. Retained source scope and quantum normals

The statements above use the actual root-quantum meridian family.
They do not identify it with a fixed-\(N\) ordinary-color quantum
normal path. On the whole \(q,M\) germ, P proves instead
\[
 S^{-1}F_\Sigma S=F_1+J_N,\qquad
 J_N=f_d^{-1}S^{-1}F_\Sigma^N(T_{0d}\otimes I).
 \tag{42}
\]
Its quantum normal generally survives. Thus a whole intertwiner
commutes with \(F_1+J_N\), not automatically with \(F_1\).
One must differentiate the unreduced matrices, the transformed
probes (14), and (42), retaining all pivot, twist and boundary
terms. Differentiating the root normal form (6) as if \(J_N=0\)
on that germ is not licensed.

The exact new conclusion is a meridian-jet reconstruction of the
original pointed source, together with a calibrated resonant
source class showing why the root constant term loses information.
Neither conclusion determines the coefficient of that class in
an original knot word, a geometric relative cycle, or a
noncancelling asymptotic contribution.

## Complete direct-source pins

* P: notes/research_relative_prefix_fourier_transition.md, SHA256
  84c15158878a2c5eb4d6e3281149ae95d36fbd2e8333bf736940d62e66d21162.
* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

Both complete directs were read nontruncated in the active author
sequence and every used implication checked. Only written mathematics
and text/hash operations were used. Frozen and public files are unchanged.
