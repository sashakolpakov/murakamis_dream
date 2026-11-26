# The actual prefix source wall at framing infinity

Private written proof, 18 November 2026.

The triangular prefix transformation of P identifies a specific
finite source wall approached by the geometric framing line at
infinity. Its first unilateral flag is unchanged as an operator.
Its cut probe, tail pivot, endpoint defect and long-transfer bands
are not unchanged: all have explicit finite formulas below.

This gives a source reduction at the wall, not its evaluated period.
In particular the scalar geometric-series limit is not a matrix
functional or a substitute for the joint long-band source.
The complete directs are P, U, M and D, pinned at the end.

## 1. The literal triangular operator and its two Cartan transforms

Use P's prefix of \(m\) actual factorial heads. Put \(d=N-1\),
\(Q=q^2\), \(x_1=-M_1/q\), and
\[
 f_j=\prod_{\ell=1}^j(1-Q^\ell),\qquad
 Z=x_1^{-1}L_1F_{\rm r},\qquad
 S=\sum_{j=0}^{d}\frac{Z^j}{f_j}.
 \tag{1}
\]
Here \(L_1w_a=w_{a-1}\) for \(a>0\), \(L_1w_0=0\), and
\(F_{\rm r},K_{\rm r}\) are the ordered coproducts on the other
prefix heads. The products \(f_j\), \(j<N\), are units on the
fixed-\(N\) normal germ of P. The endpoint convention gives
\(Z^N=0\) identically on that entire germ, not only at the root.
P proves the finite inverse
\[
 S^{-1}=\sum_{j=0}^{d}
       \frac{(-1)^jQ^{j(j-1)/2}Z^j}{f_j}.
 \tag{2}
\]

The literal weight relations imply
\[
 K_1Z=QZK_1,\qquad K_{\rm r}Z=Q^{-1}ZK_{\rm r}.
 \tag{3}
\]
For \(A(z)=\sum_{j<N}z^j/f_j\), its coefficients give
\(A(Qz)=(1-z)A(z)\) modulo \(z^N\). Substitution in (3)
therefore proves the exact ordered identities
\[
 \boxed{\quad
 S^{-1}K_1S=(I-Z)K_1,\qquad
 S^{-1}K_{\rm r}S=\mathcal R_N(Z)K_{\rm r},\qquad
 \mathcal R_N(Z)=\sum_{n=0}^{d}Q^{-n}Z^n.
 \quad}
 \tag{4}
\]
In the actual matrix algebra,
\[
                 \mathcal R_N(Z)=(I-Q^{-1}Z)^{-1}.
 \tag{5}
\]
This is a finite inverse because \(Z^N=0\). The factor in (4)
stands to the left of \(K_{\rm r}\); they need not commute.
Their product with the first transform is the unchanged total
Cartan \(K_\Sigma=K_1K_{\rm r}\), consistently with P.

The same formulas hold before root specialization. They retain
all derivatives of \(Q,x_1,F_{\rm r},K_{\rm r}\) and the
coefficients in (1)--(2). They do not replace P's off-root
raising correction \(J_N\) by zero.

## 2. The partial flag is invariant; its source defect is transported

Because \(L_1\) commutes with \(Z\),
\[
 S^{-1}L_1S=L_1,\qquad
 S^{-1}Q_{{\rm f},1}S=Q_{{\rm f},1},
                 \qquad Q_{{\rm f},1}=-q^{-1}L_1.
 \tag{6}
\]
This is U's literal inverse-free flag coupon, including its
missing lower arrow. Its exact first flag row gives
\[
 S^{-1}\mathcal E_1S
       =\big((I-Z)K_1+qM_1^{-1}I\big)Q_{{\rm f},1}.
 \tag{7}
\]
Thus no inverse of a vanishing flag denominator is used.

An invariant operator is not an invariant boundary vector.
For the constant first-head vector \(\psi=\sum_{a=0}^{d}w_a\),
\[
 (L_1-I)\psi=-w_d,\qquad
 (L_1-I)S^{-1}(\psi\otimes v)=-S^{-1}(w_d\otimes v).
 \tag{8}
\]
The last endpoint vector is explicitly
\[
 S^{-1}(w_d\otimes v)=
 \sum_{j=0}^{d}
   \frac{(-1)^jQ^{j(j-1)/2}x_1^{-j}}{f_j}
                    w_{d-j}\otimes F_{\rm r}^{\,j}v.
 \tag{9}
\]
The dual row and all other boundary data transform as well.
Equations (6)--(9) assert neither an exact finite eigenvalue-one
state for a nilpotent shift nor a full quantum eigenflag.
They specify the unchanged partial flag operator and its
unchanged, explicitly transported source equation.

## 3. Every diagonal cut and its pivotal factors

Let \(J_1w_a=aw_a\) and let
\(P_w=w(J_1)\) be any actual diagonal cut. Extend its finite
list \(w(0),\ldots,w(d)\) by zero outside that list when writing
shifted indices. Define
\[
 A_j=f_j^{-1},\qquad
 B_j=(-1)^jQ^{j(j-1)/2}f_j^{-1}.
 \tag{10}
\]
Then its full transformed probe is
\[
 \boxed{\quad
 S^{-1}P_wS
   =\sum_{\ell=0}^{d} Z^\ell
                \sum_{k=0}^{\ell}B_{\ell-k}A_k\,w(J_1-k).
 \quad}
 \tag{11}
\]
Indeed \(P_wZ^k=Z^k w(J_1-k)\). Multiplying (1)--(2)
and grouping \(j+k=\ell\) proves (11). On input \(a\),
terms with \(\ell>a\) vanish by the actual \(L_1\) endpoint;
all indices used by surviving terms lie in the finite head.

This applies in particular to the actual soft-binomial weights
\[
                  w(a)=\binom da\theta^a(1-\theta)^{d-a}.
 \tag{12}
\]
No approximation to these weights or to \(d=N-1\) occurs in
(11). For \(w(a)=1\), the reciprocal-series identity reduces
(11) to the identity operator. General cut weights do not
permit that simplification.

Every tail pivot is transformed too. For example, if the
prefix tail carries \(K_{\rm r}^{\,1-N}\), its image is
\[
       S^{-1}K_{\rm r}^{\,1-N}S
                  =\big(\mathcal R_N(Z)K_{\rm r}\big)^{1-N}.
 \tag{13}
\]
This is the ordered integer power of an invertible matrix,
not \(\mathcal R_N^{\,1-N}K_{\rm r}^{\,1-N}\).
Pivots on other heads, the cut, the word and every marked
coupon are transported together. Equation (13) is not
differentiated after substituting a root simplification.

The actual cut-current comparison follows without a new
Ward assumption:
\[
 [L_1,S^{-1}P_wS]=S^{-1}[L_1,P_w]S,\qquad
 [L_1,P_w]w_a=(w(a)-w(a-1))w_{a-1}\quad(a>0).
 \tag{14}
\]
Its \(a=0\) row is zero. For other inserted matrices one keeps
their full conjugated commutators, as in P/U. Thus preservation
of the partial flag does not erase the cut or pivotal current.

## 4. An actual prefix coordinate at geometric infinity

Fix the complete irreducible representation and its first
selected meridian flag. Some initial ordered prefix has
\[
                P^0=\begin{pmatrix}a&b\\ c&d_0\end{pmatrix},
                               \qquad c\ne0.
 \tag{15}
\]
Otherwise every prefix would be upper triangular, hence every
successive meridian, obtained by multiplying adjacent prefixes,
would preserve the selected line. That contradicts
irreducibility. No faithfulness premise is needed here.

Use M's actual selected-flag frame
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},
                      \qquad s\ne0,\quad 1+s\ne0,
 \tag{16}
\]
and set \(t=r/s\). Define
\[
                  L(t)=b+(a-d_0)t-ct^2.
 \tag{17}
\]
Multiplying \(F^{-1}P^0F\) gives its actual Gauss prefix fields
\[
 C_\Sigma=(P(r,s))_{21}=sL(t),\qquad
 K_\Sigma=(P(r,s))_{11}=C_\Sigma+ct+d_0,\qquad
 f_\Sigma=C_\Sigma/K_\Sigma.
 \tag{18}
\]
Here \(C_\Sigma\) is the principal symbol of P's ordered
\(F_\Sigma K_\Sigma\), not a new unprefixed meridian.
In particular
\[
 t=\frac{K_\Sigma-C_\Sigma-d_0}{c},\qquad
 f_\Sigma=1-\frac{cr+d_0s}{sK_\Sigma}
                    =1+\frac1r+O(r^{-2}).
 \tag{19}
\]
The expansions hold on the punctured neighborhood of infinity
where these rational coordinates are regular.

We now identify which principal wall of the actual \(S\) this
approaches. Write \(A_{\rm old},A_{\rm new}\) for its first-head
occupation clocks before and after this transformation, and \(z\)
for the commuting principal value of \(Z\). Equations (4) and
(6), together with U's \(L_1\)-symbol, give
\[
       A_{\rm old}=\frac{A_{\rm new}}{1-z},
                       \qquad p_{\rm old}=p_{\rm new}.
 \tag{20}
\]
At the root P gives \(S^{-1}F_\Sigma S=F_1\).
The actual factorial-basis symbol of \(F_1\) is
\((1-A_{\rm new})/p_{\rm new}\). On the selected classical
frame \(p_{\rm old}=1\) and fixed cut \(A_{\rm old}=A_*\ne0,1\),
these equations force
\[
 A_{\rm new}=1-f_\Sigma,\qquad
 z=1+\frac{f_\Sigma-1}{A_*}.
 \tag{21}
\]
Consequently
\[
       A_{\rm new}=-r^{-1}+O(r^{-2}),\qquad
       1-z=-\frac1{A_*r}+O(r^{-2}).
 \tag{22}
\]
Thus the geometric framing infinity approaches \(z=1\)
in this specified triangular prefix operator. It is not
obtained by equating \(r\) with an arbitrary Fourier radius.

Equations (20)--(22) describe the commuting principal chart
forced by the recorded operator relations, on their regular
locus. They do not assert a uniform symbol expansion for the
entire growing kernel \(S\) at \(z=1\). Its exact substitute
there is the finite matrix polynomial, with (8)--(14).

## 5. The simultaneous coordinates and the missing pole factor

P's exact finite Fourier transition retains all three generators,
the prefix Casimir and the carry. Its complementary coordinate
has principal value \(y=C_\Sigma\); its Cartan remains the
conjugate cyclic shift with its actual tail factor. On the
fixed classical representation,
\[
 f_\Sigma=C_\Sigma/K_\Sigma,\qquad
 e_\Sigma=
   \frac{\operatorname{tr}P^0-K_\Sigma-K_\Sigma^{-1}}{f_\Sigma}.
 \tag{23}
\]
The division in (23) is a classical regular-chart division.
It is not inversion of the finite nilpotent \(F_\Sigma\).
P supplies the exact transformed lowering operator and all
normal endpoint rows separately.

The Jacobian is also explicit. From (18),
\[
 dK_\Sigma\wedge dC_\Sigma=cL(t)\,dt\wedge ds,\qquad
 d\log K_\Sigma\wedge d\log C_\Sigma
                        =\frac{c}{K_\Sigma s}\,dt\wedge ds.
 \tag{24}
\]
D's unweighted cut form therefore has the exact expression
\[
 \Omega_{\rm cut}=-\frac{dt\wedge ds}{1+s}
  =-\frac{K_\Sigma s}{c(1+s)}
                d\log K_\Sigma\wedge d\log C_\Sigma.
 \tag{25}
\]
The quadratic growth of \(K_\Sigma\) at infinity cannot be
dropped from this comparison. Under D's positive-certificate
and marked normal hypotheses, its leading soft-cut one-form
is \(C_\beta\,dt=C_\beta\,dr/s\). Its meromorphic extension
has a double pole and zero residue at infinity. This statement
does not extend D's uniform finite-chart estimates to infinity.

In contrast \(f_\Sigma=1+1/r+\cdots\) is regular there.
For fixed \(N\), merely choosing a Fourier evaluation radius
equal to this regular function gives a matrix gauge regular
at \(r=\infty\). It cannot by itself account for the pole in
(25). Choosing the complementary radius \(C_\Sigma\) retains
the divergent coordinate, but P's exact Fourier condition
number then grows as \(|C_\Sigma|^{N-1}\). No uniform source
estimate is implied by this choice either.

## 6. The actual long-band functional of the finite inverse

There is an exact source expression for the term in (4).
Let \(\Pi_N\) be the actual diagonal soft cut times all retained
diagonal pivots, and let \(W_N\) be the full remaining marked
word, with any other scalar factors retained outside the trace.
Include all heads other than the first in a multi-index \(b\);
the prefix operators act as the identity on the other spectators.
Write \(\pi_N(a,b)\) for the diagonal entries of \(\Pi_N\).
Then
\[
 \begin{split}
 &\operatorname{Tr}\big(\Pi_NW_N\mathcal R_N(Z)K_{\rm r}\big)\\
 &\quad=
 \sum_{a=0}^{d}\sum_{b,b'}\sum_{n=0}^{a}
   \pi_N(a,b)Q^{-n}x_1^{-n}
   (W_N)_{(a,b),(a-n,b')}
                     (F_{\rm r}^{\,n}K_{\rm r})_{b',b}.
 \end{split}
 \tag{26}
\]
This follows by expanding (4) and applying the literal
\(L_1^n\) to the input. The restriction \(n\le a\) is exact.
Every intermediate other-head wall remains inside
\(F_{\rm r}^{\,n}\) and the full entries of \(W_N\).
The order \(F_{\rm r}^{\,n}K_{\rm r}\) is unchanged.

Thus the inverse is paired with a specified joint long-band
environment, not with a constant test vector. Its total degree
is zero: lowering the first head is compensated in the prefix
tail. The degree selection which kills a bare Fourier wrap
does not kill (26). It does not prove that (26) is nonzero.

For a transformed source, use the conjugates (11)--(13) and
the full transformed word instead. Equivalently pull everything
back first and apply the same finite matrix rule. One may not
keep an untransformed cut or delete the tail-pivot factor to
replace (26) by a scalar geometric series. The genuine normals
differentiate this entire expression, including its environment.

## 7. The scalar polynomial profile and its exact limitation

For a scalar variable \(z\), the polynomial in (4) obeys
\[
 \mathcal R_N(z)=\frac{1-Q^{-N}z^N}{1-Q^{-1}z}.
 \tag{27}
\]
At a physical root this is \((1-z^N)/(1-Q^{-1}z)\), with its
removable values. In particular
\[
                              \mathcal R_N(1)=0
                       \qquad(N\ge2).
 \tag{28}
\]
This does not contradict (5): the matrix inverse used the
actual relation \(Z^N=0\). Replacing it by the scalar \(z^N\)
and then deleting the numerator changes the calculation.

For completeness, (21)--(22) give a uniform scalar profile.
Put \(r=NR\), with \(R\) in a fixed compact subset of
\(\mathbb C^*\), and \(Q=e^{c_0/N}\), \(c_0=2\pi i\).
Then
\[
 z(NR)=1+\frac{\alpha(R)}N+O(N^{-2}),\qquad
 \alpha(R)=\frac1{A_*R},\qquad
 \frac{\mathcal R_N(z(NR))}{N}
   \longrightarrow
       \int_0^1e^{u(\alpha(R)-c_0)}\,du.
 \tag{29}
\]
To prove this including removable values, write
\(Q^{-1}z(NR)=\exp((\alpha-c_0)/N+O(N^{-2}))\).
Uniformly for \(0\le n<N\), its \(n\)-th power differs from
\(\exp(n(\alpha-c_0)/N)\) by \(O(N^{-1})\). The normalized
sum is the uniform Riemann sum in (29), with \(O(N^{-1})\)
error. On smaller complex compacts the same holds for fixed
derivatives by Cauchy's formula.

The limit is \((e^\alpha-1)/(\alpha-c_0)\), with its removable
value at \(\alpha=c_0\). At \(\alpha=0\) it is zero. The
\(-c_0\) term is forced by the actual coefficient \(Q^{-n}\).
It is not an optional Fourier character.

Equation (29) is a scalar polynomial limit only. The source
pairing (26) contains \(n\)-dependent bands up to order \(N\)
and the actual endpoint restrictions. Neither their replacement
by \(z^n\) nor their noncancellation is proved here. Evaluating
that joint long-band packet, and matching its currents and
normal Jacobian to the original relative cycle, is the precise
remaining source step. No framing period, scalar normalization
or nonzero geometric coefficient is inferred.

## Complete proof-source pins

* P: notes/research_relative_prefix_fourier_transition.md,
  SHA256 84c15158878a2c5eb4d6e3281149ae95d36fbd2e8333bf736940d62e66d21162.
* U: notes/research_actual_unilateral_flag_jacobi_current.md,
  SHA256 96b2fb080df630b52927063250965f2ef25a3e06e6457db9430620f31d22240c.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* D: notes/research_soft_cut_morse_bott_density.md,
  SHA256 e411f25c7b66b61d865427db1e1f789aeb09b9c76471a303dfdb8d7673fe6f9a.

All complete sources were read nontruncated in this active author
sequence, with unchanged complete reads explicitly retained where
applicable. Every used implication was checked. All new arguments
are written finite-matrix or rational calculations; no programs,
tests, or frozen/public edits were used.
