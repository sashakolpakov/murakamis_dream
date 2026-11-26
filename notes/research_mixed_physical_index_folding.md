# Exact physical-index folding and its four-type remainder

Research proof, 4 November 2026. This reflects the remaining physical
conditional indices. It is distinct from Weyl reflection of an ordinary
boundary color, and from the Racah partner-value identities. All original
finite rows, scalar factors and Fourier aliases are retained.

## 1. Factorials, physical kernels and all four folded blocks

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), and
\[
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad
 C_\epsilon(X,Y)=\sum_{j=0}^{D}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
       \qquad\epsilon=0,1.
 \tag{1}
\]
Write \(C_\epsilon[a,b]=C_\epsilon(r^a,r^b)\). The exact full
product and its reflection are
\[
                  P_D=N,\qquad P_{D-a}=N/\overline{P_a}.
 \tag{2}
\]
They follow by factoring \((X^N-1)/(X-1)\) and reflecting the
last \(a\) factors. No square root or parity convention is involved.

Let \({a\brack j}_r=P_a/(P_jP_{a-j})\), set it to zero for
\(j>a\), and let
\[
 B_{aj}=[z^j]p_a(z)
       =(-1)^j r^{j(j+1)/2}{a\brack j}_r.
 \tag{3}
\]
For a reflected physical node, exactly
\[
 p_j(r^{D-a})=
 \begin{cases}
 (-1)^j r^{-aj+j(j-1)/2}P_a/P_{a-j},&j\le a,\\
 0,&j>a.
 \end{cases}
 \tag{4}
\]
Thus reflection changes the surviving conditional support; it does not
delete a nonzero endpoint term.

**Theorem 1.** In addition to (1), the three folded physical blocks are
\[
 \begin{split}
 C_\epsilon[D-a,b]
   &=\sum_{j=0}^{D}\frac{B_{aj}p_j(r^b)}{P_j^{1+\epsilon}},\\
 C_\epsilon[a,D-b]
   &=\sum_{j=0}^{D}
       \frac{\overline{p_j(r^a)}\,
                    \overline{{b\brack j}_r}}{P_j^{1+\epsilon}},\\
 C_\epsilon[D-a,D-b]
   &=\sum_{j=0}^{\min(a,b)}
      \frac{r^{j(j-b)}{a\brack j}_r{b\brack j}_r}{P_j^\epsilon}
     =\sum_{j=0}^{D}\frac{B_{aj}\overline{B_{bj}}}{P_j^\epsilon}.
 \end{split}
 \tag{5}
\]
All conjugations here are literal conjugations of fixed root values.
The first two sums also have their exact zeros from (3)--(4) or
\(p_j(r^a)=0\) when \(a+j\ge N\).

To prove (5), insert (4) in the original finite sum. Use
\(\overline{{b\brack j}_r}=r^{-j(b-j)}{b\brack j}_r\) and
\(P_j/\overline{P_j}=(-1)^jr^{j(j+1)/2}\). These give the
displayed coefficients without any asymptotic approximation.

## 2. A genuine reflection identity for the three-type block

The original conditional coefficient identity is
\[
 P_aP_b C_0[a,b]=N[z^a]p_a(z)p_b(z).
 \tag{6}
\]
The physical root sum has no alias in this coefficient, as proved in
[the conditional finite-sum theorem](research_mixed_conditional_leg_sum.md).
Finite self-reciprocity gives
\(p_a(z)=(-1)^ar^{a(a+1)/2}z^a\overline{p_a(1/\bar z)}\).
Consequently (6) and (3) imply
\[
 C_0[a,b]=\frac{N}{\overline{P_a}P_b}
                    \sum_j\overline{B_{aj}}B_{bj}.
 \tag{7}
\]
Combining this with (5) proves the exact all-level identity
\[
 \boxed{\displaystyle
 C_0[D-a,D-b]=\frac{P_a\overline{P_b}}N\,
                       \overline{C_0[a,b]}.}
 \tag{8}
\]
This is a physical-grid identity, with the original scalar \(1/N\).

For folded indices \(0\le a\le\lfloor D/2\rfloor\), put
\(S_a=|P_a|\). Then
\[
                            S_a^2/N\le1.
 \tag{9}
\]
Indeed the consecutive factors \(2\sin(\pi a/N)\) increase up
to the midpoint, so the products first decrease and then increase;
their maximum on this range is at an endpoint. At the last endpoint
their square is \(N\) for odd \(N\) and \(N/2\) for even \(N\),
by (2). The first value is one.

Let \(E\) be any subset of these folded indices and let
\(E^*=D-E\). For every \(m\ge1\), (8) gives the whole restricted
pure-three cyclic sum
\[
 \sum_{a_1,\ldots,a_m\in E^*}\prod_v C_0[a_v,a_{v+1}]
 =\sum_{a_1,\ldots,a_m\in E}
      \left(\prod_v\frac{S_{a_v}^2}{N}\right)
                   \overline{\prod_v C_0[a_v,a_{v+1}]}.
 \tag{10}
\]
Both sides are nonnegative real: \(C_0\) is its original positive
Gram kernel. More precisely the right side is the trace of the
\(m\)-th power of \(W^{1/2}\overline{C_{0,E}}W^{1/2}\), with
\(W=\operatorname{diag}(S_a^2/N)\le I\). Its eigenvalues are
those of \(\overline{C_{0,E}}^{1/2}W\overline{C_{0,E}}^{1/2}\),
and the latter is bounded above by \(\overline{C_{0,E}}\).
The min--max principle therefore proves
\[
       0\le\operatorname{tr}(C_{0,E^*}^m)
                         \le\operatorname{tr}(C_{0,E}^m).
 \tag{11}
\]
The original pure-three scalar carries the same \(\kappa^m\) on
both sides. No new exponential normalization is introduced by this
whole physical right-half folding. Equation (11) is not asserted
for mixed three/four words or for an arbitrary pattern of right and
left coordinates within one cycle.

## 3. What changes at a four-type vertex

Use the same matrix \(B\) of polynomial coefficients and the unitary
discrete Fourier matrix
\[
 F_{jk}=N^{-1/2}r^{jk},\qquad
 D_\epsilon=\operatorname{diag}(P_j^{-\epsilon}),\qquad
 D_P=\operatorname{diag}(P_a).
 \tag{12}
\]
Let \(R\) reverse the physical row and column indices. Formula (5)
is the exact matrix identity
\[
                     R C_\epsilon R=B D_\epsilon B^*.
 \tag{13}
\]
The full-period physical Gram representation of the original
conditional sum gives, also exactly,
\[
 \frac1N D_P\overline{C_\epsilon}\,\overline{D_P}
                   =B F\overline{D_\epsilon}F^*B^*.
 \tag{14}
\]
For example, set \(E_{ai}=p_a(r^i)\), so \(E=\sqrt N BF\).
The original sum is
\(C_\epsilon=D_{\bar P}^{-1}\bar E D_\epsilon E^T D_P^{-1}\);
conjugating it proves (14). This retains its complete physical support.

For \(\epsilon=0\), (13)--(14) coincide and recover (8).
For \(\epsilon=1\), their exact difference is
\[
 R C_1R-\frac1N D_P\overline{C_1}\,\overline{D_P}
     =B\mathcal R_N B^*,\qquad
 \mathcal R_N=D_1-F\overline{D_1}F^*.
 \tag{15}
\]
The new weighted coefficient kernel in (13) is therefore not the
old four-type kernel with the three-type reflection factors.
The remainder is nonzero at every \(N\ge2\): a Fourier conjugate
of a diagonal matrix is circulant; if it is also diagonal it is
scalar, whereas the first and last entries of \(D_1\) are \(1\)
and \(1/N\).

In fact this middle remainder is exponentially large in operator norm:
\[
 \lim_{N\to\infty}\frac1N\log\|\mathcal R_N\|_2
                 =-J(1/6)>0,\qquad
 J(x)=\int_0^x\log(2\sin\pi t)\,dt.
 \tag{16}
\]
For the upper bound, \(\|\mathcal R_N\|\le2\max_jS_j^{-1}\).
Every diagonal entry of \(F\bar D_1F^*\) is the same scalar.
Hence, taking \(j\) nearest \(N/6\) and comparing its diagonal
entry with the last one,
\[
 \|\mathcal R_N\|\ge\tfrac12|P_j^{-1}-1/N|
                         \ge\tfrac12(S_j^{-1}-1/N).
 \tag{17}
\]
The elementary uniform estimate
\(\log S_j=NJ(j/N)+O(\log N)\) proves (16), since the minimum
of \(J\) is at \(1/6\). One obtains that estimate on the first
half by the upper and lower Riemann sums for the increasing function
\(\log(2\sin\pi t)\), retaining its integrable origin singularity;
reflection (2) supplies the second half. No numerical norm trend is
used. This is a norm statement about the exact middle remainder;
it is not a lower bound after the surrounding \(B\) factors or after
observation in a word.

There is also a finite obstruction to repairing (15) by arbitrary
row and column scalars. At \(N=3\), direct exact evaluation gives
\[
 C_1[1,1]\,\overline{C_1[1,0]C_1[0,1]}
       -\overline{C_1[0,0]C_1[1,1]}=-i\sqrt3/3\ne0.
 \tag{18}
\]
The first row and column of \(RC_1R\) are both identically one.
If \((RC_1R)_{ab}=u_a v_b\overline{C_1[a,b]}\) with nonzero
scalars, those row and column equations would force the left side
of (18) to vanish. Thus no such exact scalar reflection exists even
at this single level. This does not exclude a different coherent
mixed-word identity or an asymptotic estimate.

## 4. The exact Fourier weight and the off-grid qualification

Let \(d_N\) be the original polynomial of degree below \(N\) with
\(d_N(r^a)=1/P_a\), and let \(f_N\) be the polynomial of degree
below \(N\) with \(f_N(r^a)=P_a\). Write
\(f_N^\sharp(X)=\overline{f_N(1/\bar X)}\), a Laurent polynomial.
Then the following is a genuine global Laurent identity:
\[
 d_N(r^{-1}X^{-1})=\frac1N f_N^\sharp(X),\qquad
 d_N(r^{-1}X^{-1})(1+X^N)
                  =\frac1N f_N^\sharp(X)(1+X^N).
 \tag{19}
\]
The two sides of the first equality have degrees in \([-D,0]\)
and agree at all \(N\) roots by (2); this proves equality of
their coefficients. The second formula retains the full reflected
outer alias. On a folded physical node its weight is
\[
                  P_{D-a}^{-1}=\overline{P_a}/N,
 \qquad
 \frac{|P_{D-a}^{-1}|}{|P_a^{-1}|}=S_a^2/N\le1.
 \tag{20}
\]
Thus the reflected physical diagonal weight itself has no growing
relative factor on the folded half.

In contrast, (8) is only a congruence modulo
\((X^N-1,Y^N-1)\) after interpolation. It is not a Laurent
identity on arbitrary complex circles. For example at \(N=2\),
\(d_N(X)=(3+X)/4\), \(f_N(X)=(3-X)/2\), and
\[
 \begin{split}
 C_0(-X^{-1},-Y^{-1})
 -\tfrac12 f_N(X)f_N^\sharp(Y)C_0(Y,X)
 =\frac{(X+1)(Y+1)(3XY-X-5Y+3)}{32Y^2}.
 \end{split}
 \tag{21}
\]
It vanishes on the physical grid but equals \(27/128\) at
\(X=Y=2\). Similarly \(f_Nd_N\equiv1\pmod{X^N-1}\),
but the product need not be one off grid. A use of (8) in a
deformed integral therefore requires exact root projection or
the corresponding divisor currents, not equality of interpolants.

The safe full-torus operation is the literal involution
\(X\mapsto r^{-1}X^{-1}\) in the original Laurent integrand.
It preserves its constant term and sends \(1+X^{-N}\) to
\(1+X^N\); no alias is erased. A physical half-window can instead
be retained by its exact degree-below-\(N\) interpolation polynomial.
Multiplying such a window changes the Fourier bands, so the necessary
aliases must be recomputed rather than borrowed from the unwindowed
formula.

## 5. Mixed words and original boundary data

In the original physical cyclic formula, retain exactly
\[
 \operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})
 =\kappa^{m+k}N^k
   \sum_{a_1,\ldots,a_m=0}^{D}
       \prod_v C_{\epsilon_v}[a_v,a_{v+1}]
                          P_{a_{v+1}}^{-\epsilon_v}.
 \tag{22}
\]
For each chosen reflected variable replace \(a_j\) by \(D-a_j\),
use the appropriate block from (5), and replace its diagonal weight
by (20). This is an exact bijection of finite summands, with the
same \(\kappa^{m+k}N^k\). To fold a full physical sum into half
the labels, use the two elements of each reflection orbit; when
\(N\) is odd its fixed label \(D/2\) is included only once.
All one- and two-vertex incidences follow the same rule.

For open words the actual endpoint polynomials in
[the exact open composition theorem](research_mixed_conditional_torus_composition.md)
are evaluated at the reflected physical node as well. Their ordinary
boundary variables and every derivative are retained. This finite
index substitution commutes with those derivatives; it does not
assert a generic-\(q\) normal-reflection identity or remove a
peripheral factor. The color/Weyl and Racah-partner theorems concern
different source data and do not supply that missing assertion.

Thus physical right indices can be folded exactly, without a hidden
exponential scalar multiplier. For pure three cycles, (11) gives a
useful positive comparison to the left. For mixed words, the weighted
coefficient kernels (13) and their non-negligible remainder (15)
remain to be estimated coherently. Neither (16) nor (18) is a failure
of the original scalar asymptotic, and no mixed-word or knot-volume
conclusion follows from folding alone.

## 6. Reproduction

    python3 experiments/check_mixed_physical_index_folding.py

The checker uses exact cyclotomic arithmetic at levels two, three,
four and six. It checks all folded supports and kernels, the Fourier
matrix identities, actual finite cyclic scalar folding, the original
weight/alias identities, and the exact obstructions (18) and (21).
The all-level statements follow from the finite identities above.
