# A regular affine source change preserving finite colors and integral loops

Private written proof, 17 November 2026.

The older bounded-normal source-wall multiplier generally violates
perturbative color-degree regularity. A polynomial affine source change
can retain that regularity, every integral rational-loop denominator,
any prescribed finite loop jet and any prescribed finite generic-color
prefix, while changing a positive complete exponent to zero.
It also preserves ordinary root-value bounds and the actual tame
macroscopic initial-jet window.

An actual seed satisfying all premises is proved directly from the
original figure-eight Newton sum. This is a test of the sufficiency
of structural hypotheses, not a new knot-volume calculation.
No external MMR or Rozansky proof is imported. The modified family
is not asserted to be a knot invariant or to satisfy the original
full pointed operator.

## 1. Actual seed and the meaning of loop regularity

Write \(Q=q^2\), \(\varepsilon=Q-1\), and
\[
 X=Y+Y^{-1},\qquad z=X-2,\qquad \Delta(z)=1-z.
                                                               \tag{1}
\]
We denote the original reduced, zero-framed generic color, expressed
in \(Q\), by \(C_j(Q)\). The actual whole-source formulas in W and G are
\[
 \begin{split}
 F_N(Y)&=\sum_{k=0}^{N-1}\prod_{r=1}^{k}(X-Q_N^r-Q_N^{-r}),
                 \qquad Q_N=e^{2\pi i/N},\\
 C_j(Q)&=\sum_{k=0}^{j-1}\prod_{r=1}^{k}
                          (Q^j+Q^{-j}-Q^r-Q^{-r}).
 \end{split}                                                   \tag{2}
\]
They include the original scalar and all meridian normals.
In particular
\[
 F_N(Q_N^j)=C_j(Q_N)\quad(1\le j<N),\qquad F_N(1)=C_N(Q_N).
                                                               \tag{3}
\]
For the first identity, terms with \(k\ge j\) vanish because of
the factor \(r=j\); the second is direct substitution.

A loop-regular description means a series
\[
 \mathcal C(\varepsilon,z)=\sum_{n\ge0}\varepsilon^n L_n(z)
                                  \in\mathbb Q[[\varepsilon,z]]
                                                               \tag{4}
\]
whose substitution
\[
 z=z_j(\varepsilon)=(1+\varepsilon)^j
                           +(1+\varepsilon)^{-j}-2              \tag{5}
\]
gives the Taylor series of \(C_j(1+\varepsilon)\).
The integral rational-loop property is
\[
                  L_n(z)\in\frac{\mathbb Z[z]}{\Delta(z)^{2n+1}},
             \qquad L_0=1/\Delta,\quad\Delta(0)=1.               \tag{6}
\]
No convergence at the complete root sequence is included.
Since \(z_j=O(\varepsilon^2)\), substitution in (4) is formal and
well defined. Its order-\(a\) coefficient is polynomial in \(j\)
of degree at most \(a\). Hence
\[
                 \deg_j[\varepsilon^k]C_j(1+\varepsilon)\le k.
                                                               \tag{7}
\]
Indeed a contributing term \(\varepsilon^n z^\ell\) has
\(n+2\ell\le k\), and color degree at most \(k-n\).
Replacing \(\varepsilon\) by \(e^{2h}-1\) preserves (7), including
in the original \(q=e^h\) convention.

## 2. All integral rational loops from the literal Newton sum

Put
\[
 d_r(\varepsilon)=(1+\varepsilon)^r
                       +(1+\varepsilon)^{-r}-2,\qquad
 \mathcal C(\varepsilon,z)
       =\sum_{k\ge0}\prod_{r=1}^{k}(z-d_r(\varepsilon)).
                                                               \tag{8}
\]
The \(k\)-th term lies in \((\varepsilon,z)^k\), so (8) exists as
a bivariate formal series. Also \(d_r=O(\varepsilon^2)\), and
\[
 [\varepsilon^a]d_r={r\choose a}
                         +(-1)^a{r+a-1\choose a}\quad(a\ge2).
                                                               \tag{9}
\]
This is a degree-at-most-\(a\) polynomial in \(r\), integral at
all integers \(r\ge0\).

At order \(n\ge1\), choose \(\ell\le\lfloor n/2\rfloor\) factors
supplying a nonconstant \(d_r\). Thus
\[
 [\varepsilon^n]\prod_{r=1}^{k}(z-d_r)
  =\sum_{\ell=1}^{\lfloor n/2\rfloor}
                     (-1)^\ell p_{n,\ell}(k)z^{k-\ell}.         \tag{10}
\]
A term with \(k<\ell\) is zero. Explicitly \(p_{n,\ell}(k)\)
sums products of (9) over \(1\le r_1<\cdots<r_\ell\le k\)
and \(a_i\ge2,\ \sum a_i=n\).
Nested polynomial summation makes it a polynomial in \(k\)
of degree at most \(n+\ell\): each summation raises the total
input degree by at most one. Its values are integers.

If \(p(k)\) has degree at most \(b\) and integer values for \(k\ge\ell\),
the Newton expansion of \(p(j+\ell)\) in \({j\choose a}\) has integer
coefficients. Since
\[
             \sum_{j\ge0}{j\choose a}z^j=\frac{z^a}{(1-z)^{a+1}},
\]
the series \(\sum_{k\ge\ell}p(k)z^{k-\ell}\) has integer numerator
and denominator dividing \((1-z)^{b+1}\). Apply this to (10):
\[
 L_0=\frac1{1-z},\quad L_1=0,\quad
 L_n\in\frac{\mathbb Z[z]}{(1-z)^{n+\lfloor n/2\rfloor+1}}
               \subseteq\frac{\mathbb Z[z]}{(1-z)^{2n+1}}.
                                                               \tag{11}
\]
After (5), the factor \(r=j\) kills every term with \(k\ge j\).
Each \(k\)-factor term has order at least \(2k\) after substitution,
so at each Taylor order the operation is finite. It gives exactly
(2). This proves the actual loop description, the degree bound,
and the diagonal \(1/\Delta\), without an external rationality theorem.

The old multiplier \(R_J=t_J(Q,X)/t_J(Q,2)\), with
\(t_J(Q,X)=\prod_{r=1}^{J}(X-Q^r-Q^{-r})\), has
\[
 \lim_{Q\to1}R_J(Q,Q^j+Q^{-j})=\prod_{r=1}^{J}(1-j^2/r^2).
                                                               \tag{12}
\]
Thus \((1-R_J)^m\) has a degree-\(2Jm\) fixed-color limit.
Since \([\varepsilon^2](C_j-1)=j^2-1\), the old change
\(1+(1-R_J)^m(C_j-1)\) has degree \(2+2Jm\) at order two.
The following affine change avoids that failure.

## 3. A general polynomial affine surgery lemma

The lemma uses a family satisfying (3), with integral Laurent
generic colors, Weyl-symmetric whole root functions, and (4),(6).
Here \(\Delta\in\mathbb Z[z]\), \(\Delta(0)=1\), and
\(\Delta'(0)\ne0\); the seed has \(\Delta=1-z\).
For a chosen \(J\ge1\), assume also an integral prefix interpolant
\[
 S_J(Q,X)\in\mathbb Z[Q^{\pm1},X],\qquad
                S_J(Q,Q^j+Q^{-j})=C_j(Q)\quad(1\le j\le J).
                                                               \tag{13}
\]
This is supplied for the actual seed by
\[
 S_J=\sum_{k=0}^{J-1}B_k,\qquad
 B_k(Q,X)=\prod_{r=1}^{k}(X-Q^r-Q^{-r}).                         \tag{14}
\]
The factor \(r=j\) verifies (13), including \(j=J\).
No interpolation premise for arbitrary knot families is inferred.

Fix a wall depth \(m\ge1\) and a loop order \(b\ge0\) to preserve,
including order zero. Choose
\[
 K\ge b,\qquad L\ge2K+1,\qquad
 H(z)=(1-\Delta(z)^L)^m.                                       \tag{15}
\]
Define, with \(z=X-2\),
\[
 \begin{split}
 P_{\rm tr}(Q,X)&=\sum_{n=0}^{K}(Q-1)^n(1-H(z))L_n(z),\\
 B_J(Q,X)&=\prod_{j=1}^{J}(X-Q^j-Q^{-j}),\\
 V(Q,X)&=\operatorname{rem}_{B_J}
                   \bigl((1-H)S_J-P_{\rm tr}\bigr),\\
 P(Q,X)&=P_{\rm tr}(Q,X)+V(Q,X).
 \end{split}                                                   \tag{16}
\]
Because \(1-H\) is divisible by \(\Delta^L\), the first expression
is an integer polynomial in \(Q,X\). Division by the monic \(B_J\)
takes place over \(\mathbb Z[Q^{\pm1}]\). Hence \(V\) and \(P\)
belong to \(\mathbb Z[Q^{\pm1},X]\).
The new families are the single polynomial affine change
\[
 \widetilde F_N(Y)=H(Y+Y^{-1}-2)F_N(Y)+P(Q_N,Y+Y^{-1}),
 \quad
 \widetilde C_j(Q)=H(Q^j+Q^{-j}-2)C_j(Q)+P(Q,Q^j+Q^{-j}).
                                                               \tag{17}
\]

**Theorem.** This change has the following exact properties.

1. Generic colors remain integral Laurent polynomials. Every color
   \(1\le j\le J\) is unchanged. Weyl symmetry and both identities
   in (3) hold at every level, including \(N\le J\).
2. The modified loop series is regular, has integral numerator
   and denominator dividing \(\Delta^{2n+1}\) at every order \(n\),
   and agrees with the original through order \(b\).
3. \(\widetilde F_N(1)=P(Q_N,2)\to1\). Thus its complete root
   value is nonzero for large \(N\) and has exponential rate zero.
4. The exact whole germ satisfies
   \(\widetilde F_N-P(Q_N,Y+Y^{-1})=H(z)F_N(Y)\), with
\[
 [(Y-1)^{2m}](\widetilde F_N-P(Q_N,Y+Y^{-1}))
               =[-L\Delta'(0)]^mF_N(1).                       \tag{18}
\]

*Proof.* The remainder condition in (16) gives
\[
 P(Q,a_j(Q))=(1-H(a_j(Q)-2))C_j(Q),\quad
                  a_j(Q)=Q^j+Q^{-j},\quad 1\le j\le J.
                                                               \tag{19}
\]
This proves the exact prefix; (17) proves integrality, symmetry,
and all root compatibilities by substitution. There is no
small-level exceptional definition or division.

It remains to control the remainder at \(\varepsilon=0\), without
dividing by coalescing color differences. Put
\[
 \delta_j(\varepsilon)=a_j(1+\varepsilon)-2=O(\varepsilon^2),
 \qquad
 \mathscr A=\mathbb Z[[\varepsilon]][z]\big/
                   \prod_{j=1}^{J}(z-\delta_j(\varepsilon)).    \tag{20}
\]
This is a free module on \(1,z,\ldots,z^{J-1}\). Every nonleading
coefficient of its defining monic polynomial lies in
\(\varepsilon^2\mathbb Z[[\varepsilon]]\), so
\(z^J\in\varepsilon^2\mathscr A\). In particular
\(z^{Jk}\in\varepsilon^{2k}\mathscr A\). Thus reduction extends
continuously to \(\mathbb Z[[\varepsilon,z]]\) and preserves every
\(\varepsilon\)-adic order. The denominator \(\Delta(z)\) is a unit
in this algebra because \(\Delta(0)=1\) and \(z\) is topologically
nilpotent.

For the seed, the Newton series reduces to \(S_J\) exactly: every
\(B_k\) with \(k\ge J\) is a multiple of \(B_J\). The same conclusion
holds under the stated general premises. Indeed reduce
\(\mathcal C-S_J\) to its polynomial of degree less than \(J\).
Evaluation at \(z=\delta_j\) is continuous and gives zero by
(5),(13). The \(J\) nodes are distinct over \(\mathbb Q((\varepsilon))\),
since
\(\delta_j-\delta_i=(j^2-i^2)\varepsilon^2+O(\varepsilon^3)\).
The reduced polynomial is therefore zero. Consequently
\[
 V=\operatorname{rem}_{B_J}\left[
        (1-H)\left(\mathcal C-
                     \sum_{n=0}^{K}\varepsilon^nL_n\right)\right]
                        \quad\hbox{in }\mathscr A,             \tag{21}
\]
and order preservation gives
\[
                  V=O(\varepsilon^{K+1})
                    =O(\varepsilon^{b+1})
                        \quad\hbox{coefficientwise in }X.      \tag{22}
\]
The finite monic remainder in (16) and this formal class agree
in the free basis, so (22) applies to the already integral Laurent
polynomial \(V\). No loss depending on the prefix length occurs.

Define \(\widetilde{\mathcal C}=H\mathcal C+P(Q,2+z)\). Then
\[
 \widetilde{\mathcal C}-\mathcal C
   =(H-1)\left(\mathcal C-\sum_{n=0}^{K}\varepsilon^nL_n\right)+V
                   =O(\varepsilon^{b+1}).                     \tag{23}
\]
The series is regular and specializes to the Taylor series of (17).
At every order, multiplication by the fixed integer \(H(z)\) and
addition of \(P\), whose \(\varepsilon\)-coefficients are integer
polynomials in \(z\), preserve the denominator \(\Delta^{2n+1}\)
and its integral numerator. Thus (7) also holds.
Equations (22),(23) give \(P(1,2)=L_0(0)=1\), because \(H(0)=0\).
This proves the third assertion. Finally
\[
 H(z)=[-L\Delta'(0)]^m z^m+O(z^{m+1}),\qquad z=(Y-1)^2/Y
\]
proves (18). \(\square\)

## 4. Actual growth, ordinary values, and initial normal jets

For the seed, the original complete value is
\[
 F_N(1)=\sum_{k=0}^{N-1}\prod_{r=1}^{k}4\sin^2(\pi r/N),\qquad
 \frac1N\log F_N(1)\longrightarrow
       \Gamma=\int_0^{5/6}\log(4\sin^2(\pi t))\,dt>0.            \tag{24}
\]
W, Section 6, proves this through both parities by uniform Riemann
summation with \(O(\log N)\) endpoint error and positivity.
The primitive \(s\mapsto\int_0^s\log(4\sin^2\pi t)\,dt\)
has its unique global maximum at \(5/6\).
Thus (17) changes a genuine positive complete exponent to zero,
while (18), with \(\Delta'(0)=-1\), retains that exponent as
the exact higher normal \(L^mF_N(1)\).

The original ordinary values have the uniform polynomial bound in
B, Section 1. The fixed polynomials \(H,P\) are uniformly bounded
on \(|Q|=|Y|=1\), so (17) preserves that bound with a constant
multiplier and an additive constant. No new power of \(N\) is required.

G, Section 4, also gives polynomial bounds for every fixed-order
\(q\)-jet, uniformly on
\[
                       1\le j\le\lfloor(N+1)/2\rfloor.          \tag{25}
\]
These bounds survive (17). Indeed, after \(Q=q^2,Y=q^{2j}\),
each fixed \(q\)-derivative of a monomial of \(H\) or \(P\)
costs at most a fixed power of \(N\), uniformly for \(j<N\).
For the scaled parameter \(q=q_N(1+s/N)\), every fixed derivative
of these fixed multipliers is \(O(1)\), since \(j/N\le1\).
Leibniz and (25) give the asserted bound. This uses the actual
initial-window jet theorem, not a full ordinary-color jet bound
or a new positive Hilbert-space realization.

## 5. What data have and have not been preserved

For the seed there is also an integral Newton expansion. The identity
\[
       X B_k=B_{k+1}+(Q^{k+1}+Q^{-k-1})B_k                    \tag{26}
\]
shows that multiplication by the fixed polynomial \(H(X-2)\)
is a finite-band operation with integer Laurent coefficients.
The polynomial \(P\) has a finite integral expansion in the monic
basis \(B_k\). Hence \(H\sum_{k\ge0}B_k+P\) has integral Laurent
Newton coefficients. These are coefficientwise finite expressions;
after color substitution the sum terminates, and at a root of
unity and \(X=2\), \(B_N=0\). No completion or knot-realization
claim is needed for this assertion.

If the original family is \(q\)-holonomic, so is (17).
Multiplication by a fixed rational function of \(Q,Y\) and addition
of a rational section preserve that property: subtract the section,
apply an original annihilator, annihilate its rational right side
with a first-order rational shift, and clear fixed denominators.
B, Section 3, gives this same elementary recurrence construction.

Off the zeros of \(H\), the nonconstant sections obey the rational
gauge relation \(\widetilde F-P=HF\). At a generic fixed \(Y\),
\(H(QY)/H(Y)\to1\) as \(Q\to1\); here \(H(Y)\) means
\(H(Y+Y^{-1}-2)\). Conjugation therefore retains an existing
principal characteristic factor on this localized chart.
An added rational section may introduce an abelian factor;
no equality of minimal operators is asserted.

Unlike the older multiplier, the affine map (17) is polynomial
and regular at \((Q,Y)=(1,1)\). Its linear coefficient \(H\)
is not a unit at the complete wall. The exact prefix is retained
by its additive term \(P\), rather than by requiring the linear
coefficient to equal one on each prefix curve. This is why the
intersection of those curves with the complete wall is consistent.

For comparison, a fixed rational affine normalization cannot change
a positive complete exponential rate if its linear coefficient does
not vanish identically on the wall. More precisely, let
\(U(Q,Y),V(Q,Y)\) be fixed rational functions with well-defined
restrictions \(u(Q)=U(Q,1)\) and \(v(Q)=V(Q,1)\), and suppose
\(u\not\equiv0\). Their Laurent germs at \(Q=1\) give, for all
large \(N\), polynomial upper bounds for \(|u(Q_N)|\), its inverse,
and \(|v(Q_N)|\). If \(N^{-1}\log|F_N(1)|\to\Gamma>0\), the
triangle inequality in both directions then yields
\[
 \frac1N\log|u(Q_N)F_N(1)+v(Q_N)|\longrightarrow\Gamma.        \tag{27}
\]
This is a statement about fixed rational normalizations, not arbitrary
\(N\)-dependent units. For example a fixed peripheral factor
\(1+Y^a\) restricts to two. The construction (17) violates exactly
the hypothesis \(u\not\equiv0\), because \(H(0)=0\) identically
along the complete wall, although \(H\) is regular there.

The theorem retains integral generic colors, all integral rational
loop denominators, the perturbative degree bound, the Alexander
diagonal, any fixed finite loop and color prefixes, ordinary
root-value bounds and the actual tame initial-jet window.
It does not retain the original full operator, its complete
pointing, or all perturbative coefficients simultaneously.
The modified family is not asserted to arise from another knot.
Consequently this is neither a new volume-conjecture case nor a
counterexample for an actual knot. It proves that the listed
structural data alone do not force the original complete growth.
That inference requires additional control of the specified
source at its nonunit complete wall.

## Direct sources and proof audit

The complete direct texts were read, their used implications checked,
and their hashes renewed:

* B: [Bounded-source normal transfer](bounded_normal_color_transfer.md),
  SHA256 6a464af6842c60b8c845d1dc52d8b3f7c105ce9e93c323a3c8bea4b04a6277dc.
  Actual ordinary-value bounds, the older wall change, and
  rational-affine recurrence closure.
* G: [Actual ordinary-color normal jets](actual_figure_eight_ordinary_normal_jets.md),
  SHA256 380e4300b0a9efb6db2a9a4cd1967ef56d4c4ec83392d96bb86452679abfb814.
  Generic-color Newton identity, reduced zero-framed convention,
  and the actual macroscopic initial-jet bound.
* W: [Actual whole source](figure_eight_whole_source_identity.md),
  SHA256 63738069644ac40aa05fcb860e2de8edbb09c06ac2976f522cc1c3acc94e3951.
  Whole root identity with all meridian normals and the positive
  complete growth proof used in (24).

No external rationality theorem or MMR proof is imported.
Only written mathematics, source reads and hashes were used.
No mathematical program, test or build was run. Previously frozen
notes and public manuscripts were unchanged.
