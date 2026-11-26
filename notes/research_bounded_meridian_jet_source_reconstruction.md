# A bounded meridian jet for the original pointed source

Private written proof, 18 November 2026.

The whole-meridian reconstruction in C can be sharpened uniformly
in the level and the number of tensor heads. At a fixed primitive
quantum root, the original pointed source of an analytic family of
actual intertwiners is determined by its transformed constant
coefficient through meridian order at most two. Together with C,
the upper bound is \(\min(N-1,2)\).

The proof constructs the full generic intertwiner from explicit
highest seeds and dual rows. Its known source kernel has two
possible simple-pole factors: a pairwise total-Casimir collision
and one vanishing lowering coefficient. Multiplicities, absent
weights, the original cut and the pivotal trace are retained.
There is no assumption that an arbitrary constant coefficient is
admissible, and no scalar replacement of the remaining Casimir.

This is a bound on the required meridian jet, not a uniform norm
bound, a minimal-depth assertion, or an evaluation of a knot
source. Quantum normals still require the unreduced whole germ.

The sole complete direct C is the prefix commutant and pointed
normal functional. The spectral construction and pole count are
proved below.

## 1. Actual operators and the constant coefficient

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(m\ge1\) actual balanced heads. Vary their common meridian \(M\)
near one, keeping \(q\) fixed. On each head,
\[
 K_iw_a=xQ^{-a}w_a,\qquad x=-M/q,
 \quad F_iw_a=(1-Q^{a+1})w_{a+1}\quad(a<d),
 \tag{1}
\]
\[
 \mathcal E_iw_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0).
 \tag{2}
\]
The missing endpoint arrows are zero. Write
\(K_{\rm r},F_{\rm r},\mathcal E_{\rm r}\) for the ordered
remaining-head coproducts, with the empty tensor interpreted as
\(K_{\rm r}=I,F_{\rm r}=\mathcal E_{\rm r}=0\).

Let \(S\) be C's actual triangular prefix operator. With
\(f_a=\prod_{j=1}^a(1-Q^j)\),
\[
 S=\sum_{j=0}^{d}\frac{(x^{-1}L_1F_{\rm r})^j}{f_j},
 \qquad L_1w_a=w_{a-1},\quad L_1w_0=0.
 \tag{3}
\]
Both \(S\) and its finite inverse are analytic near \(M=1\).
C proves
\[
 S^{-1}F_\Sigma S=F_1,\qquad
 K_\Sigma=K_1K_{\rm r},\qquad [S,K_\Sigma]=0,
 \tag{4}
\]
\[
 E':=S^{-1}\mathcal E_\Sigma S
   =I\otimes\mathcal E_{\rm r}+L_1b_A,\qquad
 b_a=MK_{\rm r}Q^{-a}-M^{-1}K_{\rm r}^{-1}.
 \tag{5}
\]
The second term is evaluated at the input occupation \(a\) and
is zero at \(a=0\). The actual total Casimir becomes
\[
 \Omega':=S^{-1}\Omega_\Sigma S
       =F_1\otimes\mathcal E_{\rm r}
                -I\otimes(MK_{\rm r}+M^{-1}K_{\rm r}^{-1}).
 \tag{6}
\]
It commutes with \(F_1,E',K_\Sigma\).

The additional nilpotence needed below is exact:
\[
                              (E')^N=0.
 \tag{7}
\]
Indeed the original coproduct is
\(\mathcal E_\Sigma=\sum_i\mathcal E_iK_{i+1}\cdots K_m\).
Its ordered summands pairwise \(Q\)-commute. The primitive-root
binomial identity therefore makes its \(N\)-th power the sum
of the \(N\)-th powers of those summands. Each is zero because
\(\mathcal E_i^N=0\). One can prove the binomial identity by the
finite coefficient recursion: all intermediate coefficients
contain \(1-Q^N\), with denominators
\(\prod_{j=1}^a(1-Q^j)\), \(a<N\), which are units.
This uses primitivity, not parity or primality of \(N\).

Let \(W(M)\) be an analytic family commuting with the three
actual total generators. C gives uniquely
\[
 W':=S^{-1}WS=\sum_{n=0}^{d}F_1^n\otimes B_n,\qquad
                         [B_0,K_{\rm r}]=0.
 \tag{8}
\]
The matrices \(B_n\) of an actual \(W\) are analytic. They obey
C's full lowering recursion and final closing row. We do not
assert that an arbitrary analytic \(B_0\) satisfies those
conditions.

## 2. Weight spaces and simple Casimir collisions

Put
\[
 x_{\rm r}=(-M/q)^{m-1},\quad
 k_a=x_{\rm r}Q^{-a},\quad z_a=Mk_a,\quad
 \lambda_a=-z_a-z_a^{-1},\qquad 0\le a<N.
 \tag{9}
\]
Let \(U_a\) be the constant remaining-head occupation subspace
whose total occupation is congruent to \(a\) modulo \(N\).
Then \(K_{\rm r}|_{U_a}=k_a I\). The spaces may have arbitrary
multiplicity in the arguments below; zero spaces are retained.
For the empty tensor, \(U_0=\mathbb C\) and the others are zero.
Write
\[
 i_a:U_a\longrightarrow V,\quad i_av=w_0\otimes v,
 \qquad
 p_a:V\longrightarrow U_a
 \tag{10}
\]
for the embedding and the projection onto first occupation zero
and remaining weight \(a\), where \(V\) is the full tensor space.
The block \(B_{0,a}\) denotes \(B_0|_{U_a}\).

The total Casimir satisfies the exact polynomial identity
\[
                     \prod_{a=0}^{d}(\Omega'-\lambda_a I)=0.
 \tag{11}
\]
To prove it, restrict to one eigenspace of \(K_\Sigma\), whose
eigenvalue is \(\kappa\). On its first-occupation \(l\) grade,
the remaining \(K\)-eigenvalue is \(\kappa x^{-1}Q^l\).
As \(l=0,\ldots,d\), these run once around the list of \(k_a\).
Equation (6) is block bidiagonal with respect to these grades:
its diagonal is the corresponding scalar \(\lambda_a\), and
its other term raises \(l\) by one. Order the \(N\) commuting
factors in (11) in this grade order. Each successive factor
kills the first remaining graded piece. After \(N\) steps
the result is zero. Missing grades cause no difficulty.

For \(a\ne b\),
\[
 \lambda_a-\lambda_b
       =-(z_a-z_b)\left(1-\frac1{z_az_b}\right).
 \tag{12}
\]
The first factor is a unit near \(M=1\). Since
\(z_a=(-q^{-1})^{m-1}M^mQ^{-a}\), a collision at \(M=1\)
occurs precisely when
\[
                       a+b\equiv-(m-1)\pmod N.
 \tag{13}
\]
For each \(a\) there is at most one distinct such \(b\).
At a collision the derivative of the second factor in (12)
is \(2m\), so the collision is simple. If (13) gives \(a=b\),
there is no collision with a distinct label.

Choose a sufficiently small punctured meridian disk on which
the \(\lambda_a\)'s are distinct. Define the actual matrices
\[
             \mathsf P_a
              =\prod_{b\ne a}
                    \frac{\Omega'-\lambda_b I}{\lambda_a-\lambda_b}.
 \tag{14}
\]
Equation (11) and elementary polynomial interpolation imply
that these are mutually orthogonal projectors summing to \(I\).
They commute with \(F_1,E',K_\Sigma\), and
\(\Omega'\mathsf P_a=\lambda_a\mathsf P_a\).
By (12)--(13), each \(\mathsf P_a\) has a meromorphic
continuation with pole order at most one at \(M=1\).
An absent weight simply gives the zero projector, as also
follows from the rank calculation below.

The first-row action is
\[
                         p_b\mathsf P_a=\delta_{ab}p_b.
 \tag{15}
\]
Indeed the first-row action of \(\Omega'\) is the diagonal
\(-MK_{\rm r}-M^{-1}K_{\rm r}^{-1}\).
The diagonal first-occupation blocks of \(\mathsf P_a\) are
the projections onto \(U_a\). Thus its trace, and hence rank
on the punctured disk, is
\[
                          \operatorname{rank}\mathsf P_a
                                      =N\dim U_a.
 \tag{16}
\]
No simplicity of that multiplicity space is assumed.

## 3. Highest seeds and the exact dual rows

Define the meromorphic seed
\[
                         J_a=\mathsf P_a i_a.
 \tag{17}
\]
It begins in first occupation zero with coefficient \(v\):
\(p_aJ_a=I_{U_a}\). The vectors
\[
                  F_1^lJ_av,\qquad
                    0\le l<N,\quad v\in U_a,
 \tag{18}
\]
are linearly independent. Their first possible nonzero
occupation row is \(l\), with coefficient \(f_l v\).
They lie in \(\operatorname{im}\mathsf P_a\), and (16) shows
that they form a basis of that entire summand.

The seed is an actual highest seed:
\[
                                 E'J_a=0.
 \tag{19}
\]
Here is a proof that keeps the possible top wrap until it is
excluded. The seed has total \(K\)-weight \(xk_a\).
Since \(E'\) raises that weight by \(Q\), its image can only
be the \(l=d\) component in the basis (18). Thus
\(E'J_a=F_1^dJ_a T_a\) for a matrix \(T_a\) on \(U_a\).
The commutator
\([E',F_1]=(q-q^{-1})(K_\Sigma-K_\Sigma^{-1})\)
gives, for \(1\le l<N\),
\[
 E'F_1^lJ_a=\epsilon_{a,l}F_1^{l-1}J_a,\qquad
 \epsilon_{a,l}=(1-Q^l)(z_aQ^{-l}-z_a^{-1}).
 \tag{20}
\]
The possible term \(F_1^lE'J_a\) is zero for these \(l\).
For a direct evaluation of the commutator sum, use
\(xk_a=-z_a/q\) and sum the two geometric progressions
in \(Q^{\pm l}\); they give exactly (20).

All \(\epsilon_{a,l}\) are nonzero on a smaller punctured
disk. By (7),
\[
 0=(E')^NJ_a
      =\left(\prod_{l=1}^{d}\epsilon_{a,l}\right)J_aT_a.
 \tag{21}
\]
The product is a unit there and \(J_a\) is injective. Hence
\(T_a=0\), proving (19). No endpoint is silently closed.

Set
\[
 c_{a,0}=1,\qquad c_{a,l}=\prod_{j=1}^{l}\epsilon_{a,j}.
 \tag{22}
\]
Equations (19)--(20) and the first-row projection give the
exact duality
\[
 p_a(E')^l F_1^kJ_b
       =\begin{cases}
           c_{a,l}I_{U_a},&a=b,\ k=l,\\
           0,&\text{otherwise}.
         \end{cases}
 \tag{23}
\]
For \(k>l\), a positive first occupation remains. For \(k<l\),
the lowering reaches the highest seed and then vanishes.
For \(k=l\), its remaining first row has weight \(b\).
In particular the exact identity operator is
\[
                I_V=\sum_{a=0}^{d}\sum_{l=0}^{d}
                  F_1^lJ_a c_{a,l}^{-1}p_a(E')^l.
 \tag{24}
\]

## 4. Reconstruction of the whole actual intertwiner

The action of \(W'\) on a highest seed is
\[
                              W'J_a=J_aB_{0,a}.
 \tag{25}
\]
It commutes with \(\mathsf P_a,K_\Sigma,E'\).
Within the basis (18), its total weight selects only \(l=0\).
Its first row is \(B_{0,a}\), by (8), (15), and (17).
This proves (25) without declaring \(B_{0,a}\) arbitrary.
Commuting \(W'\) with \(F_1\) and applying (24) yields
\[
 \boxed{\quad
 W'=\sum_{a=0}^{d}\sum_{l=0}^{d}
     F_1^lJ_a B_{0,a}\,c_{a,l}^{-1}p_a(E')^l .
 \quad}
 \tag{26}
\]
This is a full matrix identity on the punctured disk.
There is only one spectral projector in each term, inside
\(J_a\). A second projector on the dual row is unnecessary:
\(p_a(E')^l\mathsf P_a=p_a(E')^l\), by (15) and
\([E',\mathsf P_a]=0\).

## 5. The original source kernel and the two-pole bound

Let \(g_{\rm r}=K_{\rm r}^{1-N}\), and keep the original
highest-cut source
\[
              \Phi_0(W)=\operatorname{Tr}_V
                          ((P_0\otimes g_{\rm r})W).
 \tag{27}
\]
All unchanged crossing scalar, framing and peripheral factors
remain in \(W\) or multiply this exact functional as originally
prescribed. Define on \(U_a\)
\[
 \boxed{\quad
 H_a^{(2)}(M)=
 \sum_{l=0}^{d}c_{a,l}^{-1}
   p_a(E')^l S^{-1}(P_0\otimes g_{\rm r})S
                      F_1^l\mathsf P_ai_a .
 \quad}
 \tag{28}
\]
The superscript records a pole-order bound, not a derivative.
Using (26) and the finite rectangular trace identity
\(\operatorname{Tr}_V(AB)=\operatorname{Tr}_{U_a}(BA)\) gives
\[
 \boxed{\quad
                  \Phi_0(W(M))
                    =\sum_{a=0}^{d}
                        \operatorname{Tr}_{U_a}
                              (H_a^{(2)}(M)B_{0,a}(M)).
 \quad}
 \tag{29}
\]
The order of the cut, pivot, \(S\), and all dual rows in
(28) is part of this identity. They are not reset.

Each \(c_{a,l}^{-1}\) has pole order at most one at \(M=1\).
Indeed a factor in (20) vanishes there only if
\[
                         j\equiv-(m-1)-2a\pmod N.
 \tag{30}
\]
Among \(1,\ldots,l<N\), there is at most one such \(j\).
Its derivative is
\(2m(1-Q^j)z_aQ^{-j}\), a nonzero number at the zero.
All other factors in (20) are units.
The projector in (28) has pole order at most one by (12)--(14).
Every other matrix in (28) is analytic. Therefore
\[
                         \operatorname{pole}_{M=1}
                                  H_a^{(2)}\le2.
 \tag{31}
\]
This bound is independent of \(N\), \(m\), and the weight
multiplicities. The sizes of coefficients and the permissible
meridian disk are not asserted to be uniform.

The left side of (29) is analytic for the actual family \(W\).
Its prescribed value at completeness is consequently
\[
 \Phi_0(W(1))=[t^0]\sum_{a=0}^{d}
       \operatorname{Tr}_{U_a}
           (H_a^{(2)}(1+t)B_{0,a}(1+t)).
 \tag{32}
\]
Only the Taylor coefficients of \(B_0\) through order two
can enter. C separately gives order at most \(N-1\).
Thus the source is determined by order at most
\[
                              \min(N-1,2).
 \tag{33}
\]
We do not claim that the particular kernel (28) has the
smaller pole order when \(N=2\); (33) combines two exact
reconstructions. Nor is a lower bound on the necessary jet
depth proved.

Replacing \(P_0\otimes g_{\rm r}\) in (28) by any specified
analytic finite source matrix gives the same two-pole bound
for its pairing with the same actual intertwiner. In particular
the whole prescribed soft cut can be retained. This does not
put an arbitrary marked word into the homogeneous commutant:
its nonzero Ward defects must still be carried separately.

## 6. Scope at the quantum root

All decompositions in this note take place at fixed \(q_N\)
and on the whole common-meridian family. On the full fixed-\(N\)
quantum normal germ, C retains instead
\[
 S^{-1}F_\Sigma S=F_1+J_N,\qquad
 J_N=f_d^{-1}S^{-1}F_\Sigma^N(T_{0d}\otimes I).
 \tag{34}
\]
The normals of this row, the original probes, and all pivots
cannot be obtained by differentiating (26) as if \(J_N=0\)
off the root. The ordinary-color path is a separate restriction
of those unreduced whole operators.

The new result is an explicit fixed-order meridian source
functional. It supplies neither a bound on the resulting
second-jet source as \(N\) grows nor a map to a geometric
framing cycle. In particular it does not choose a nonzero
geometric period, suppress retained boundary currents, or
show that a constant coefficient belongs to the image of
the actual knot braid.

## Complete direct-source pin

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  SHA256 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.

The complete direct was freshly read nontruncated in the active
author sequence and every used implication checked. Only written
mathematics and text/hash operations were used. Frozen and public
files are unchanged.
