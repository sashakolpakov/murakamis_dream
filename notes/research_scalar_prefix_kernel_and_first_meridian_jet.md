# The scalar prefix kernel and the original first-meridian-jet source

Private written proof, 18 November 2026.

The universal kernel in C loses its remaining-head Casimir dependence
exactly. At a fixed primitive quantum root it is
\[
 \boxed{\qquad
 \mathfrak h_N(k,\omega;M)=\frac{D_N(M)}{D_N(Mk)},\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \qquad}                                                     \tag{1}
\]
Here \(D_N\) is its Laurent-polynomial continuation at \(z=\pm1\),
and (1) is a rational identity, not a prescription to evaluate an
uncancelled denominator at a zero.

For the actual common-meridian family, this gives an explicit
first-jet formula for the original highest-cut, pivotal source.
Its functional cost in the actual occupation basis is polynomial
in \(N\) at fixed tensor width. Neither the constant coefficient
nor its derivative is estimated here. The proof uses finite
matrix paths, a finite product telescope, and polynomial
interpolation; it imports no modified-trace theorem.

The sole complete direct is C, pinned at the end. The moment
argument and finite telescope were independently developed with
Early; all calculations needed for the conclusion are included.

## 1. The universal kernel and its two-head realization

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
Keep \(q\) fixed throughout. A head with meridian \(M_i\) has
\[
 K_iw_a=x_iQ^{-a}w_a,\quad x_i=-M_i/q,\qquad
 F_iw_a=(1-Q^{a+1})w_{a+1},\qquad
 E_iw_a=(M_iQ^{-a}-M_i^{-1})w_{a-1}.                         \tag{2}
\]
The outward endpoint arrows vanish. We write \(E_i\) for C's
scaled lowering operator \(\mathcal E_i\). The head Casimir is
\(\omega_i=q x_i+q^{-1}x_i^{-1}=-M_i-M_i^{-1}\).

For an ordered tensor prefix, C gives the analytic triangular
operator \(S\), preserving the total Cartan, such that
\[
 S^{-1}F_\Sigma S=F_1,\qquad
 S^{-1}E_\Sigma S=E_{\rm r}+L_1b_A,\qquad
 b_j=MK_{\rm r}Q^{-j}-M^{-1}K_{\rm r}^{-1},                  \tag{3}
\]
where \(M=M_1\). An actual total intertwiner \(W\) has
\[
 S^{-1}WS=\sum_{n=0}^dF_1^n\otimes B_n,\qquad
 [K_{\rm r},B_0]=0,\qquad
 B_n=-\frac{b_n^{-1}[E_{\rm r},B_{n-1}]}{1-Q^n}             \tag{4}
\]
where these inverses exist. Its original pointed source is
\[
 \Phi_0(W)=\operatorname{Tr}((P_0\otimes K_{\rm r}^{1-N})W)
 =\operatorname{Tr}_{\rm r}
       \left(K_{\rm r}^{1-N}\sum_{n=0}^d x_1^{-n}F_{\rm r}^nB_n\right).
                                                                  \tag{5}
\]
The cut and pivot in (5) are the original ones, with no additional
pivot on the opened head.

For reference, the scalar kernel of C is defined as follows:
\[
 u(k,\omega)=\omega-qk-q^{-1}k^{-1},\qquad
 b_j(k)=MkQ^{-j}-M^{-1}k^{-1},\qquad
 a_{n,n}(k,\omega)=Q^{-n}k^{1-N},                            \tag{6}
\]
\[
 a_{n,j-1}(k,\omega)=\frac1{1-Q^j}
 \left\{
 \frac{u(Q^{-j}k,\omega)a_{n,j}(k,\omega)}{b_j(k)}
 -\frac{u(k,\omega)a_{n,j}(Qk,\omega)}{b_j(Qk)}
 \right\},\quad j=n,\ldots,1,
                                                                  \tag{7}
\]
\[
 \mathfrak h_N(k,\omega;M)=\sum_{n=0}^d x_1^{-n}a_{n,0}(k,\omega).
                                                                  \tag{8}
\]
It is rational in \(k,M\) and polynomial of degree at most \(d\)
in \(\omega\). With the full remaining Casimir
\(\Omega_{\rm r}=F_{\rm r}E_{\rm r}+qK_{\rm r}+q^{-1}K_{\rm r}^{-1}\),
the exact source functional is
\[
 \Phi_0(W)=\operatorname{Tr}_{\rm r}
       \big(\mathfrak h_N(K_{\rm r},\Omega_{\rm r};M)B_0\big).
                                                                  \tag{9}
\]

We will use (9) on two heads with independent generic meridians.
This does not require extending C's common-meridian pole claim.
Indeed (3)--(5) hold with independent meridians, and the adjoint
of the recursion in (4), for the ordinary trace pairing, is
\[
 A\longmapsto\frac{[E_{\rm r},A b_j^{-1}]}{1-Q^j}.
                                                                  \tag{10}
\]
Using \(FE=u(K,\Omega)\), \(EF=u(Q^{-1}K,\Omega)\), and the
weight relations in this adjoint gives precisely (6)--(9).
Thus (9) holds on the generic two-parameter set where the
displayed denominators are nonzero. These are finite rational
matrix identities in independent nonzero \(M_1,M_2\), so they
extend algebraically beyond an initial neighborhood of one.
No Borel continuation or source-cycle transport is used when
an auxiliary second color is moved around its root orbit.

## 2. Closed first-head paths and the pivotal moments

Take a second head whose highest Cartan value is an independent
\(k_0\ne0\), so \(M_2=-qk_0\) and
\(\omega_2=qk_0+q^{-1}k_0^{-1}\). Write \(K=K_2\).
The ordered coproducts are
\[
 F_\Sigma=F_1+K_1^{-1}F_2,\qquad
 E_\Sigma=E_1K_2+E_2,\qquad K_\Sigma=K_1K_2.
\]
Expanding the actual total Casimir and collecting only commuting
head factors gives
\[
 \Omega_\Sigma
 =K_1^{-1}\omega_2+
   \big(\omega_1-(q+q^{-1})K_1^{-1}\big)K
   +F_1E_2+K_1^{-1}E_1F_2K.                                \tag{11}
\]
All endpoint rows remain those of (2).

For every \(0\le p\le d\), the first-head highest block
\(\langle0|\Omega_\Sigma^p|0\rangle\) is a polynomial in \(K\)
of degrees \(0,\ldots,p\). Its coefficient of \(K^p\) is
independent of \(\omega_2\) and \(k_0\).

Here is a finite path proof, including the degree assertion.
Set \(X=E_2\), \(Y=F_2K\). The tail letters satisfy
\[
 KX=QXK,\qquad KY=Q^{-1}YK,
\]
\[
 XY=u(Q^{-1}K,\omega_2)K,\qquad
 YX=Q\,u(K,\omega_2)K.                                   \tag{12}
\]
Both products in (12) are polynomials in \(K\) of degrees
zero through two, with their degree-two coefficient independent
of \(\omega_2\). A nonzero first-head path from occupation zero
back to zero has equally many upward and downward steps, say
\(r\) of each. Its remaining \(p-2r\) steps are diagonal.
Move their tail polynomials through \(X,Y\) by the weight
relations. Every balanced word in \(X,Y\) has an adjacent
opposite pair. Removing such pairs with (12) inductively gives
a polynomial of degree at most \(2r\), with no negative powers.
The diagonal factors add degree at most \(p-2r\).
To reach degree \(p\), every factor must contribute its top
degree, whose coefficient contains no \(\omega_2\).
All first-head path coefficients depend only on \(M,q\).
Forbidden paths are simply zero, so no endpoint correction
is removed in this argument.

Since the second-head eigenvalues are \(k_0Q^{-a}\),
\[
 \operatorname{Tr}(K^{1-N+j})=0\quad(0\le j<d),\qquad
 \operatorname{Tr}(K^{1-N+d})=N.                          \tag{13}
\]
Consequently the original source moments satisfy
\[
 \Phi_0(\Omega_\Sigma^p)=0\quad(0\le p<d),\qquad
 \Phi_0(\Omega_\Sigma^d)=C_N(M),                           \tag{14}
\]
where \(C_N(M)\) is independent of the second-head meridian.
No positive or cyclic replacement of the original source was
used: (13) is the literal pivotal trace of the highest block.

## 3. Lagrange coupons and the exact phase factor

Put
\[
 k_a=k_0Q^{-a},\quad z_a=Mk_a,\quad
 \lambda_a=-z_a-z_a^{-1},\qquad 0\le a<N,
\]
\[
 P(t)=\prod_{a=0}^d(t-\lambda_a).
                                                                  \tag{15}
\]
Work first where these \(N\) values are distinct. Let
\[
 f_a(t)=\frac{\prod_{b\ne a}(t-\lambda_b)}{P'(\lambda_a)}.
                                                                  \tag{16}
\]
The actual coupon \(W_a=f_a(\Omega_\Sigma)\) is an intertwiner.
In the \(S\) coordinates the Casimir is
\[
 S^{-1}\Omega_\Sigma S
   =F_1E_2-I\otimes(MK+M^{-1}K^{-1}).
                                                                  \tag{17}
\]
Therefore its constant coefficient is
\(B_0=f_a(-MK-M^{-1}K^{-1})=|a\rangle\langle a|\).
Equation (9), and separately the leading coefficient of (16)
with (14), give
\[
 \mathfrak h_N(k_a,\omega_2;M)
       =\Phi_0(W_a)=\frac{C_N(M)}{P'(\lambda_a)}.            \tag{18}
\]
The remaining-head projector has ordinary trace one; there
is no additional factor \(N\) in (18).

The derivative in (18) has a direct product evaluation. Since
the \(z_b\)'s run around the roots with common \(N\)-th power,
\[
 \begin{split}
 P'(\lambda_a)
 &=(-1)^d\prod_{b\ne a}(z_a-z_b)
                  \prod_{b\ne a}(1-z_a^{-1}z_b^{-1})\\
 &=(-1)^d N z_a^{N-1}
                  \frac{1-z_a^{-2N}}{1-z_a^{-2}}
   =(-1)^d N D_N(z_a).
 \end{split}                                             \tag{19}
\]
The calculation is initially on its generic domain and hence
holds by rational continuation. It fixes the phase as well
as the magnitude.

## 4. The finite telescope and polynomial interpolation

Evaluate (7) at \(\omega_0=qk+q^{-1}k^{-1}\).
Then \(u(k,\omega_0)=0\), so every second term in the downward
recursion at that fixed \(k\) vanishes. Direct factorization gives
\[
 \frac{u(Q^{-j}k,\omega_0)}{(1-Q^j)b_j(k)}
   =x_1\,\frac{1-k^2Q^{1-j}}{1-M^2k^2Q^{-j}}.
                                                                  \tag{20}
\]
Put \(r=Q^{-1}\), \(a=k^2\), \(b=M^2k^2r\), and use
\((a;r)_n=\prod_{j=0}^{n-1}(1-ar^j)\). Equations (6)--(8)
become
\[
 \mathfrak h_N(k,\omega_0;M)
      =k^{1-N}\sum_{n=0}^{N-1}r^n
                       \frac{(a;r)_n}{(b;r)_n}.            \tag{21}
\]
This sum telescopes without an infinite-series identity.
For \(T_n=(a;r)_n/(b;r)_n\) and
\(U_n=(1-br^{n-1})T_n\), including \(U_0=1-b/r\),
\[
 U_{n+1}-U_n=r^n(b/r-a)T_n,\qquad
 T_N=\frac{1-a^N}{1-b^N}.
                                                                  \tag{22}
\]
As \(r^N=1\), \(U_N=(1-b/r)T_N\). Summing (22) and
substituting the parameters in (21) gives
\[
 \mathfrak h_N(k,\omega_0;M)
 =k^{1-N}\frac{(1-b/r)(T_N-1)}{b/r-a}
 =\frac{D_N(M)}{D_N(Mk)}.                                 \tag{23}
\]
All intermediate divisions are made generically; the resulting
identity is rational, including the removable parameter values.

Apply (23) to (18) with \(a=0\), so \(k=k_0\), and use (19).
It follows that
\[
                         C_N(M)=(-1)^d N D_N(M).
                                                                  \tag{24}
\]
Thus (18) proves the desired value for every weight of every
generic second head.

Finally fix independent generic \(k,M\). For each \(a\) choose
the second-head highest value \(k_0=Q^a k\). Its weight \(a\)
is \(k\), and its Casimir is
\[
                    \omega_a=qQ^a k+q^{-1}Q^{-a}k^{-1}.
                                                                  \tag{25}
\]
These \(N\) numbers are distinct for generic \(k\): equality
for different labels requires a fixed exceptional value of
\(k^2\). The polynomial in \(\omega\) in (8) has degree at
most \(N-1\), and (18),(24) give the same claimed value at
all \(N\) nodes (25). Polynomial interpolation proves (1)
over the rational function field in \(k,M\), hence identically.
There is no assumption about a scalar or semisimple remaining
Casimir in this conclusion. Evaluating this rational-polynomial
identity at the commuting matrices \(K_{\rm r},\Omega_{\rm r}\)
retains all their weight multiplicities and Casimir Jordan blocks.

## 5. The common-meridian first-jet row

Return to \(m\ge1\) actual heads with common meridian \(M\), and
an analytic family \(W(M)\) of total intertwiners. Set
\[
 K_0=K_{\rm r}(1),\qquad K_{\rm r}(M)=M^{m-1}K_0,\qquad
 \varepsilon=(-1)^{(N+1)(m-1)}.
                                                                  \tag{26}
\]
The empty remaining tensor has \(K_0=I\) and \(\varepsilon=1\).
The actual root weights give
\((MK_{\rm r})^N=\varepsilon M^{mN}I\).
Combining (1) and (9) gives, on a punctured meridian disk,
\[
 \boxed{\quad
 \Phi_0(W(M))=
 \frac{D_N(M)}
      {\varepsilon(M^{mN}-M^{-mN})}
 \operatorname{Tr}_{\rm r}
      \big((MK_{\rm r}-M^{-1}K_{\rm r}^{-1})B_0(M)\big).
 \quad}                                                     \tag{27}
\]
This is the original source, not a new normalization. Its left
side is analytic. The denominator has a simple zero at one,
where \(D_N(1)=N\), so admissibility forces the exact residue row
\[
                 \operatorname{Tr}_{\rm r}
                       ((K_0-K_0^{-1})B_0(1))=0.
                                                                  \tag{28}
\]
The removable value of (27) is consequently
\[
 \boxed{\quad
 \Phi_0(W(1))=
 \frac1{2\varepsilon}
      \operatorname{Tr}_{\rm r}((K_0+K_0^{-1})B_0(1))
 +\frac1{2\varepsilon m}
      \operatorname{Tr}_{\rm r}((K_0-K_0^{-1})B_0'(1)).
 \quad}                                                     \tag{29}
\]
Indeed the derivative of the denominator in (27) is
\(2\varepsilon mN\); differentiate its trace numerator using
(26). Equation (28) removes every term involving the derivative
of \(D_N\) or the regular part of the scalar prefactor.
Both the sign \(\varepsilon\) and the factor \(m\) are retained.
For \(m=1\), (29) reduces to the scalar value of \(B_0\), as it
should.

The derivative in (29) is that of the actual constant coefficient
of \(S(M)^{-1}W(M)S(M)\). It includes the meridian dependence of
the entire triangular transform. An arbitrary pair of matrices
called \(B_0,B_0'\) need not satisfy (28) or the other exact
intertwiner conditions in C.

Equip the actual remaining occupation basis in (2) with its
standard \(\ell^2\) norm. At the complete root \(K_0\) is
diagonal unitary, and the remaining dimension is \(N^{m-1}\).
The elementary bound
\(|\operatorname{Tr}(AB)|\le N^{m-1}\|A\|\|B\|\) and
\(\|K_0\pm K_0^{-1}\|\le2\) give
\[
 \boxed{\quad
 |\Phi_0(W(1))|
 \le N^{m-1}\big(\|B_0(1)\|+m^{-1}\|B_0'(1)\|\big).
 \quad}                                                     \tag{30}
\]
This controls the cost of the explicit functional in that
original basis. It bounds neither these two source matrices
nor the condition number of \(S\). Any separately prescribed
external framing or peripheral scalar multiplies the original
functional unchanged and must also be retained in its bound.

## 6. Source and normal scope

The collapse (1) is a universal rational identity for C's
kernel. Equations (27)--(30) apply to its actual analytic
common-meridian intertwiner families at fixed \(q_N\).
Inserted marks that fail to commute with the total generators
retain their Ward defects; they are not declared homogeneous
intertwiners to use this reconstruction.

On a whole quantum-normal germ, C instead retains
\(S^{-1}F_\Sigma S=F_1+J_N\), whose \(q\)-normal need not
vanish. The whole source, cut, pivotal and framing adapters
must be differentiated before any such specialization.
The root-meridian identities above are not ordinary-color
closed-source quantum-normal identities.

No knot-word estimate, source noncancellation, framing-cycle
pushforward, or nonzero geometric coefficient follows from
(29) or (30). The new conclusion is the exact Casimir-free
kernel and its explicitly controlled first-meridian-jet
functional for the original pointed source.

## Complete direct-source pin

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  SHA256 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.

The complete direct was read nontruncated in the active author
sequence. All used implications and source orders were checked.
Only written mathematics and text/hash operations were used;
frozen and public files are unchanged.
