# Preserving the coherent boundary rate on nearby physical colors

Research proof, 7 November 2026. The type-three conditional kernel
has an exact first-order recurrence which propagates its value at a
period endpoint to the nearby physical colors. The exponential cost
tends to zero with the width of this discrete interval. Thus taking
absolute values of the original summation rows is unnecessary there.
The result concerns physical root-of-unity values of the outgoing
variable. It does not assert a bound on a complex neighborhood of that
interval, or the remaining comparison with the geometric action.

## 1. The original kernel and an auxiliary finite sum

Fix an integer level \(N\ge2\), and put
\[
 r=e^{-2\pi i/N},\qquad
 P_j=(r;r)_j=\prod_{a=1}^j(1-r^a),\qquad
 S_j=|P_j|,\qquad P_0=S_0=1.
 \tag{1}
\]
The original type-three kernel is
\[
 C_{0,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rY;r)_j}{P_j^2},\qquad X\ne0.
 \tag{2}
\]
Keep its entire finite support. Define the polynomial
\[
 G_X(z)=\sum_{j=0}^{N-1}\frac{(rX;r)_j}{P_j}z^j,
 \qquad H_k(X)=G_X(r^k/X),\qquad
 F_N(X)=\frac{X^{-N}-1}{N}.
 \tag{3}
\]
In particular \(H_0(X)=C_{0,N}(X,1)\).

**Lemma 1.** For \(0\le k<N-1\),
\[
 (1-r^{k+1})H_{k+1}(X)
       =(1-r^k/X)H_k(X)+F_N(X).
 \tag{4}
\]
For every \(0\le b<N\),
\[
 C_{0,N}(X,r^b)
   =\sum_{k=0}^{b}
       \frac{(-1)^k r^{k(k+1)/2}}{P_kP_{b-k}}H_k(X).
 \tag{5}
\]
These are identities for the original finite functions at both level
parities.

*Proof.* Write \(a_j=(rX;r)_j/P_j\). Its exact coefficient
recurrence is
\(a_j(1-r^j)=a_{j-1}(1-r^jX)\) for \(1\le j<N\).
Coefficient comparison, including the last coefficient, therefore gives
\[
 (1-z)G_X(z)=(1-rXz)G_X(rz)-\frac{1-X^N}{N}z^N.
 \tag{6}
\]
Here \(P_{N-1}=N\) and
\((rX;r)_{N-1}=(1-X^N)/(1-X)\), with the removable value
at \(X=1\), account for the last term. Substitute \(z=r^k/X\)
and use \(r^{kN}=1\). This proves (4), with its forcing term.

For every original row, including those which vanish, one has
\[
 \frac{(r^{b+1};r)_j}{P_j}
       =\frac{(r^{j+1};r)_b}{P_b}.
 \tag{7}
\]
If \(j+b<N\), this follows by cancelling factors of \(P_{j+b}\).
If \(j+b\ge N\), both numerators in (7) contain \(1-r^N\),
whereas \(P_j,P_b\) are nonzero. The finite product expansion gives
\[
 \frac{(r^{j+1};r)_b}{P_b}
   =\sum_{k=0}^b
     \frac{(-1)^k r^{k(k+1)/2}r^{jk}}{P_kP_{b-k}}.
 \tag{8}
\]
Substitute (8) into (2) and interchange the two finite sums.
The inner sum is exactly \(H_k(X)\). This proves (5).
\(\square\)

The recurrence starts with the coherently summed value \(H_0\).
Its forcing is retained even when the value of \(H_0\) is small.
Neither (4) nor (5) divides by that value.

## 2. A uniform bound on the discrete interval

Fix a compact annulus \(\mathcal B\subset\mathbb C^*\), and set
\[
 A=1+\sup_{X\in\mathcal B}|X|^{-1},\qquad
 B=A+2,\qquad D=\max\{B,2A\}.
 \tag{9}
\]
For \(0<\delta\le1/4\), define
\[
 f(\delta)=\delta\log\frac{e}{4\delta},\qquad
 \omega(\delta)=3f(\delta)+\delta\log D.
 \tag{10}
\]
In particular \(\omega(\delta)\to0\) as \(\delta\downarrow0\).

**Theorem 2.** For \(0\le b\le\lfloor\delta N\rfloor\),
\[
 |C_{0,N}(X,r^b)|
 \le (N+1)\bigl(|C_{0,N}(X,1)|+|F_N(X)|\bigr)
                       e^{N\omega(\delta)}.
 \tag{11}
\]
For \(1\le b\le\lfloor\delta N\rfloor\), the other end of
the physical period satisfies
\[
 |C_{0,N}(X,r^{N-b})|
               \le N e^{N\omega(\delta)}.
 \tag{12}
\]
Both bounds are uniform for \(X\in\mathcal B\).

*Proof.* Iterating (4) and using \(|1-r^k/X|\le A\) gives
\[
 |H_k|\le \frac{A^k}{S_k}|H_0|
       +\frac{|F_N|}{S_k}
                  \sum_{m=0}^{k-1}A^{k-1-m}S_m
 \le\frac{B^k}{S_k}(|H_0|+|F_N|).
 \tag{13}
\]
For the last inequality use \(S_m\le2^m\) and
\(\sum_{m=0}^{k-1}A^{k-1-m}2^m\le(A+2)^{k-1}\).
The case \(k=0\) is immediate.

For \(1\le j\le\delta N\), concavity of sine on
\([0,\pi/2]\) and \(j!\ge(j/e)^j\) give
\[
 S_j=\prod_{a=1}^j2\sin(\pi a/N)
       \ge (4/N)^j j!,\qquad
 S_j^{-1}\le\exp\left\{N f(j/N)\right\}
       \le e^{Nf(\delta)}.
 \tag{14}
\]
The last inequality follows from
\(f'(t)=\log(1/(4t))\ge0\) on \((0,1/4]\).
It also holds at \(j=0\).
Apply (13) to (5). Each term is bounded by
\((|H_0|+|F_N|)B^k/(S_k^2S_{b-k})\).
There are at most \(N+1\) terms, and (14) bounds the three
reciprocal factorials. This proves (11).

For (12), the factor \((r^{N-b+1};r)_j\) vanishes for
\(j\ge b\). For the surviving rows,
\[
 |X^{-j}(rX;r)_j|\le A^j,\qquad
 |(r^{N-b+1};r)_j|\le2^j.
\]
Thus the entire original kernel is bounded by
\(\sum_{j<b}(2A)^j/S_j^2\). Equation (14) proves (12),
with the slightly larger common function (10). \(\square\)

## 3. The coherent endpoint rate

Let \(X=e^{-2\pi iz}\), \(z=y+ic\), on a fixed compact
subset of \(0<y<1\). The exact endpoint identity in
[the boundary-strip calculation](research_mixed_boundary_strip_bounds.md)
is
\[
 C_{0,N}(X,1)=N\overline{d_N(1/\overline X)}.
 \tag{15}
\]
The [absolute Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
therefore gives, for every \(\eta>0\), an upper rate
\[
 M_0(z)=\max\{-\Re g(\overline z),\ 2\pi\max(-c,0)\}
 \tag{16}
\]
for (15), with a uniform polynomial prefactor and rate tolerance
\(\eta\). The function \(g\) and its branches are those of
the cited theorem. Also
\[
 |F_N(X)|\le\frac2N e^{2\pi N\max(-c,0)}.
 \tag{17}
\]
Since \(M_0\ge0\), Theorem 2 proves the same upper rate
\(M_0(z)+\omega(\delta)+\eta\) on both physical intervals
\[
 Y=r^b,\quad 0\le b\le\delta N,
 \qquad\text{or}\qquad
 Y=r^{N-b},\quad 1\le b\le\delta N.
 \tag{18}
\]
In particular a strict geometric comparison at the exact endpoint,
if proved uniformly on the relevant reference set, has room to absorb
this cost for sufficiently small fixed \(\delta\).

An outgoing diagonal weight may be retained as well. At the physical
nodes, \(d_N(r^b)=1/P_b\). For any fixed nonnegative power
\(\sigma\), its modulus on the first interval costs at most
\(\sigma f(\delta)\) in the rate, by (14). On the second
interval the exact root-product complement gives
\[
 S_{N-b}S_{b-1}=N,
 \qquad |d_N(r^{N-b})|=S_{b-1}/N\le2^{b-1}/N.
 \tag{19}
\]
Its cost is at most \(\sigma\delta\log2\). All these costs
tend to zero. At the nodes the additional Fourier factor
\(1+Y^{-N}\) equals two; it is not an omitted exponential term.
This is a statement about evaluating a literal factor. In the exact
node-averaging identity of Section 6, its two Fourier sectors are
already incorporated into a single node weight; no extra factor two
is inserted there.

## 4. Use in an exact contraction and its limitations

The original conditional attachment already has a physical-node
formula. With its incoming type \(\alpha\) and attached type
\(\beta\), it is
\[
 (\mathcal T_{\alpha\beta}F)(Y)
   =\sum_{a=0}^{N-1}\frac{F(r^a)C_{\beta,N}(r^a,Y)}{P_a^\alpha}.
 \tag{20}
\]
The [literal transfer theorem](research_mixed_literal_transfer_norm_obstruction.md)
proves this formula with its full Fourier weights and both parities.
Thus a physical interval can be split off after an exact contraction;
it need not first be replaced by a complex contour collar. Other
variables can remain in their exact finite functions. To use (11) in
a particular word, its orientation, adjacent factors, weights and
normalization must still be retained as in (20).

Theorem 2 is stated with the second variable at physical nodes;
Section 5 gives its first-variable counterpart. Neither statement is
a type-four endpoint theorem, a bound for arbitrary complex seam
variables, or a proof of the geometric comparison above. In particular a
sum of absolute values of the original rows can have a strictly
larger endpoint rate than (16); that stronger rate is not substituted
for the coherently summed initial value in this argument.

No numerical evaluation is used. The proof consists of the finite
identities (4)--(8), elementary factorial bounds, and the previously
established absolute estimate for the actual Fourier polynomial.

## 5. The opposite type-three orientation

The same discrete collar estimate applies when the physical variable
is the first argument of the original type-three kernel. Set
\(p_j(X)=(rX;r)_j\) and
\(\tau_j=(-1)^j r^{j(j+1)/2}\). Termwise one has
\[
 \overline{p_j(1/\overline X)}=\tau_j^{-1}X^{-j}p_j(X),
 \qquad \overline{P_j}=\tau_j^{-1}P_j,
 \qquad
 C_{0,N}(X,Y)=
       \overline{C_{0,N}(1/\overline Y,1/\overline X)}.
 \tag{21}
\]
Every factor \(\tau_j\) cancels in the last identity. Since
\(1/\overline{r^b}=r^b\), it follows that
\[
 C_{0,N}(r^b,X)=\overline{C_{0,N}(1/\overline X,r^b)},
 \qquad C_{0,N}(1,X)=N d_N(X).
 \tag{22}
\]
Apply Theorem 2 on the reflected compact annulus
\(\{1/\overline X:X\in\mathcal B\}\). If
\(X=e^{-2\pi iz}\), \(z=y+ic\), its endpoint rate is
\[
 M_1(z)=M_0(\overline z)
        =\max\{-\Re g(z),\ 2\pi\max(c,0)\}.
 \tag{23}
\]
Thus on either physical collar the first-variable kernel has upper
rate \(M_1(z)+\widetilde\omega(\delta)+\eta\), where the
reflected-annulus function \(\widetilde\omega\) also tends to zero.
At the upper physical end, the stronger rate tending to zero in
(12) remains available for this orientation as well.

No such reciprocity conclusion is made for \(C_{1,N}\). Its
additional reciprocal factorial leaves a factor \(\tau_j\) after
the conjugation in (21), so the displayed cancellation is specific
to type three.

## 6. Exact partial node averaging in the original word

This discrete estimate can be used before deforming the other
variables. Consider the literal conditional source of
[torus composition](research_mixed_conditional_torus_composition.md),
or its exactly contracted form
[with the full terminal polynomial](research_mixed_contracted_finite_boundary_windows.md).
Fix one retained variable \(Y\), of type \(3+\varepsilon\).
Remove only its own diagonal and alias factors and denote the
remaining integrand by \(\mathscr R_N(Y;\mathbf X)\).
Its \(Y\)-band is contained in \([-N+1,N-1]\): an incoming
kernel or cap has nonnegative band, while the outgoing kernel or
terminal polynomial has nonpositive band. All other variables and
their original Fourier alternatives remain in \(\mathbf X\).

There is the exact identity
\[
 \begin{split}
 &N\operatorname{CT}_Y\!\left[
   \mathscr R_N(Y;\mathbf X)
        \{d_N(Y)(1+Y^{-N})\}^{\varepsilon}\right]\\
 &\hspace{15mm}=
   \sum_{b=0}^{N-1}\frac{\mathscr R_N(r^b;\mathbf X)}{P_b^\varepsilon}.
 \end{split}
 \tag{24}
\]
For \(\varepsilon=0\), the only multiple of \(N\) in that
band is zero. For \(\varepsilon=1\), multiplication by \(d_N\)
puts the band in \([-N+1,2N-2]\); node averaging selects its
coefficients of degrees zero and \(N\). The two terms of
\(1+Y^{-N}\) select precisely those same coefficients under
\(\operatorname{CT}_Y\). Finally \(d_N(r^b)=1/P_b\).
This proves (24) without dropping a Fourier alternative or doubling
its node weight. It is not an identity for either of the two
four-type sectors separately.

Let
\[
 \begin{split}
 B_\delta={}&\{0,\ldots,\lfloor\delta N\rfloor\}\,
       \cup\{N-\lfloor\delta N\rfloor,\ldots,N-1\},\\
 \sum_{b<N}&=\sum_{b\in B_\delta}+\sum_{b\notin B_\delta}.
 \end{split}
 \tag{25}
\]
The second set in \(B_\delta\) is empty when
\(\lfloor\delta N\rfloor=0\). Equation (25) is an exact
partition of the finite source after (24); it is not a claim that a
truncated node sum equals a truncated contour arc. Each resulting
summand is still a Laurent polynomial in the remaining variables.
Their contours may therefore be deformed independently, even with
the choice depending on \(b\), while preserving winding numbers
and the original normalization. Replacing an unnormalized
\(\operatorname{CT}_Y\) by the sum in (24) carries the displayed
factor \(1/N\); no outside scalar is changed silently.

If the two factors incident to the physical coordinate are both
type-three kernels, Theorem 2 and (22) apply simultaneously to
\(C_{0,N}(X,r^b)C_{0,N}(r^b,Z)\). Their upper rates are the
sum of the respective coherent endpoint rates and two costs tending
to zero. The finite node sum contributes only a polynomial factor.
An incident type-four kernel or terminal message is not covered by
that assertion and retains its own source obligation. The weights
at the averaged node are exactly those in (24), and their small
factorial costs are controlled by (14) and (19).

In particular this representation permits the neighboring cap
variable to stay at its original height while the type-three seam
coordinate is handled on physical nodes. The actual geometric
reference is unchanged; a node is a target, not a newly admissible
reference. The original complex marginal terms, and the correct
zero or one representative for either side of the physical period,
must still be retained in any geometric comparison.

All steps apply at both level parities and commute with fixed
ordinary-color derivatives. This establishes a legitimate discrete
boundary representation and its coherent kernel bounds. It does
not establish their calibrated sign, control the complementary
node set in (25), or turn them into a complex seam-collar theorem.
