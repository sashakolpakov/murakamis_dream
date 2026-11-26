# A weighted conditional estimate and the first physical end rectangle

Research deduction, 7 November 2026. The finite binomial formula gives
a uniform weighted absolute-row bound for an entire conditional
operator. Combined with exact termination of the first cap, it pays
the last one percent of the first sampled coordinate in the next
attachment \(34\to343,344\), while the second coordinate ranges over
its entire physical period. Both Fourier coefficients are retained
through their exact root sum. No numerical evaluation is used.

## 1. A complete weighted conditional operator bound

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(S_j=|P_j|\), and \(p_j(Z)=(rZ;r)_j\). The actual conditional
kernel is
\[
 C_{\beta,N}(Y,Z)=\sum_{j=0}^{D}
       \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
                    \qquad \beta\in\{0,1\}.
                                                               \tag{1}
\]
Let
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 c_{\rm b}=-2J(1/6)<1/3 .
                                                               \tag{2}
\]
The original uniform sine-product estimate and reflection give
\[
 \log S_j=NJ(j/N)+O(\log N),\quad
 |J(t)|\le c_{\rm b}/2,\qquad 0\le j<N,\quad0\le t\le1.
                                                               \tag{3}
\]
The strict bound in (2) follows from the sine chord
\(2\sin\pi u>6u\) on \(0<u<1/6\).

The finite binomial estimate in
[global transform ends, Section 2](research_mixed_three_four_global_transform_ends.md)
is
\[
 \frac{p_j(Z)}{P_j}
  =\sum_{k=0}^{j}
       \frac{(-1)^kr^{k(k+1)/2}Z^k}{P_kP_{j-k}},
 \qquad
 \frac{|p_j(Z)|}{S_j}
  \le C N^A e^{N\{c_{\rm b}+\log_+|Z|\}} .
                                                               \tag{4}
\]
This is zero-safe and valid at every \(j<N\).

At \(Y=r^b\), only \(j+b<N\) remain. Consequently
\[
 \frac{|C_{\beta,N}(r^b,Z)|}{S_b}
 \le\sum_{j=0}^{D-b}
       \frac{S_{b+j}}{S_b^2S_j^{1+\beta}}
                            \frac{|p_j(Z)|}{S_j}.
                                                               \tag{5}
\]
By (3), the first quotient in (5) has rate at most
\((4+\beta)c_{\rm b}/2\). Combining with (4), and summing all
physical rows, proves
\[
 \boxed{\displaystyle
 \sum_{b=0}^{D}\frac{|C_{\beta,N}(r^b,Z)|}{S_b}
       \le C N^A
          e^{N\{1+\beta/6+\log_+|Z|\}}.}
                                                               \tag{6}
\]
No internal row or revived outgoing numerator is removed. There
is no nonvanishing assumption on \(C_{\beta,N}\) or \(p_j(Z)\).

For example, if a prescribed row \(R_{b,N}\) obeys
\(\max_b|R_{b,N}|\le L_N\), the original weighted transfer obeys
\[
 \left|\sum_b\frac{R_{b,N}}{P_b}C_{\beta,N}(r^b,Z)\right|
       \le L_N C N^A
             e^{N\{1+\beta/6+\log_+|Z|\}} .
                                                               \tag{7}
\]
This is an absolute upper estimate, not a coefficient lower bound.
Fixed output derivatives are allowed on smaller bounded disks by
Cauchy's formula, applied to each finite row before summing.

The two actual output types have useful different radial ranges:
\[
 \begin{array}{c|c}
 \beta=0& \Im z\le3/40,\quad Z=e^{-2\pi iz},\\
 \beta=1& \Im z\le0.
 \end{array}                                                   \tag{8}
\]
Both ordinary and terminal actual output images are strictly inside
their respective ranges. This follows from
[ordinary heights](research_mixed_cyclic_critical_height_bounds.md)
and [private endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md).
On (8) the exponent in (6) is uniformly below \(103/70\):
for \(\beta=0\), it is at most \(1+3\pi/20<103/70\);
for \(\beta=1\), it is \(7/6<103/70\).

## 2. The exact first-root decomposition

Retain
\[
\begin{split}
 U_{0,N}(w,X)
   &=\sum_{\ell=0}^{D}\frac{H_N(w,r^{-\ell})}{P_\ell}p_\ell(X),\\
 F_N(w,Y)&=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)].
\end{split}                                                    \tag{9}
\]
The first factor has degree at most \(D\), and the second has
\(X\)-band contained in \([-D,0]\). Thus their product has band
in \([-D,D]\), with no nonzero multiple of \(N\), and exactly
\[
                       F_N(w,Y)
       =\sum_{a=0}^{D}U_{0,N}(w,r^a)C_{1,N}(r^a,Y).
                                                               \tag{10}
\]
The next source is therefore the complete double root sum
\[
 \mathcal F_{\beta,N}(w,Z)
  =\sum_{a,b=0}^{D}
       U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                       \frac{C_{\beta,N}(r^b,Z)}{P_b}.
                                                               \tag{11}
\]
The exact old-four weight and both Fourier coefficients are
already included in the second root sum, by
[the next-attachment identity](research_mixed_three_four_next_conditional_attachment.md),
equations (3)--(5). No extra \(N\), \(\kappa_N\), selection factor
or Gram matrix is inserted in (10)--(11).

Define the first physical end rectangle
\[
 \mathcal R_{\beta,N}(w,Z)
  =\sum_{a=\lceil99N/100\rceil}^{D}\sum_{b=0}^{D}
       U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                       \frac{C_{\beta,N}(r^b,Z)}{P_b}.
                                                               \tag{12}
\]
The inner range is the full physical period.

## 3. The first two factors have a small rate on that rectangle

Put \(v=1-a/N\le1/100\). The exact terminating first-cap formula
and its uniform physical bound are
[physical far-half, equations (7)--(8), (20)](research_mixed_three_four_physical_far_half.md):
\[
 U_{0,N}(w,r^a)=\frac{N}{P_a^2}
       \sum_{\ell=0}^{D-a}(-q)^{-\ell}e_\ell(w)
                                    \frac{P_{a+\ell}}{P_\ell^2},
 \qquad
 |U_{0,N}(w,r^a)|
    \le C_\tau N^A
        e^{N\{2v\log2-3J(v)+\tau\}} .
                                                               \tag{13}
\]
Here \(q=e^{\pi i/N}\). The proof is uniform through the true
last row. It holds for a sufficiently small fixed complex
ordinary-color disk about \(-2\).
It also holds for all real ordinary colors: the terminating support
has \(\ell/N\le v<1/2\), where the zero-safe Newton entropy obeys
\(V_\theta\le V_0\). This is the same explicit all-real extension
used in [physical middle reduction, Section 1](research_mixed_three_four_physical_middle_reduction.md).

For every physical \(b\), the other first-coordinate factor obeys
\[
 C_{1,N}(r^a,r^b)
   =\sum_{j=0}^{D-a}
        \frac{r^{-aj}P_{a+j}}{P_aP_j^3}p_j(r^b).
                                                               \tag{14}
\]
Some further terms vanish when \(j+b\ge N\); keeping them with
their exact zero causes no problem. Since \(|p_j(r^b)|\le2^j\)
and \(t=j/N<v\), its uniform row rate is at most
\[
 J(v)-J(v-t)-3J(t)+t\log2
                          \le-3J(v)+v\log2 .
                                                               \tag{15}
\]
The chirp has modulus one. Equations (13)--(15) bound the entire
product, uniformly over every \(b\), by the rate
\[
                        3v\log2-6J(v)+\tau .
                                                               \tag{16}
\]
Use \(2\sin\pi u\ge6u\) on \([0,1/6]\). Then
\[
 -J(v)\le v(1-\log(6v))
       \le\frac1{100}\left(1+\log\frac{50}{3}\right)
                              <\frac1{25}.
                                                               \tag{17}
\]
For the last inequality,
\(e^3>\sum_{j=0}^{5}3^j/j!=92/5>50/3\).
Also \(3v\log2<21/1000\). Hence the complete rate in (16),
before its arbitrary tolerance, is strictly below
\[
                         \frac{261}{1000}.             \tag{18}
\]

## 4. Payment of the whole second sampling cycle

Apply (6) to (12), after using the uniform first-product bound
(18). The number of first physical rows is only a polynomial
factor. On the two corresponding output domains (8), the total
rate is strictly below
\[
 \frac{261}{1000}+\frac{103}{70}
             =\frac{12127}{7000}<\frac74 .
                                                               \tag{19}
\]
The reserve is \(123/7000\). Choose the total color/source
tolerance in (13) smaller than this reserve.

**Theorem 1.** The sum of the absolute values of the original
products in (12) satisfies
\[
 \sum_{a=\lceil99N/100\rceil}^{D}\sum_{b=0}^{D}
 \left|U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                         \frac{C_{\beta,N}(r^b,Z)}{P_b}\right|
                   \le C N^A e^{7N/4}.                \tag{20}
\]
It holds at both parities, for all real ordinary colors and on a
sufficiently small fixed complex disk about \(-2\), and for the
corresponding closed radial output domains (8).
All physical supports and numerator zeros are retained.

The [next physical-end theorem, Section 3](research_mixed_three_four_next_physical_end_sector.md)
proves, independently of this row bound, that every actual next
ordinary or terminal conditional action satisfies
\(\Re\mathcal P_\beta^+(-2,z)>15/8\).
Choose uniform small neighborhoods of the compact actual output
families on which the respective radial hypotheses (8) still hold
and \(\Re\mathcal P_\beta^+(w,z)>29/16\). On smaller neighborhoods,
\[
 \left|\partial_w^j\partial_z^k
   \left[e^{-N\mathcal P_\beta^+(w,z)}
      \mathcal R_{\beta,N}(w,e^{-2\pi iz})\right]\right|
            \le C_{j,k}N^{A_{j,k}}e^{-N/32}.           \tag{21}
\]
For complex colors and output parameters this follows by Cauchy's
formula. For real ordinary colors, fixed color derivatives in
(20) follow by applying Markov's inequality to the complete
polynomial \(U_{0,N}(w,r^a)\) before summing, and comparing with
the complete-color action. No ordinary normal is replaced by an
outgoing raw-coordinate derivative.

This theorem deletes a rectangle of actual indices from (11),
not a piece of a continuous two-variable torus. It may be combined
with the separate final-second-coordinate deletion by a disjoint
partition or by its positive bounds; their overlap is not a new
source term. The other indices, all contour currents needed to
represent them, and the distinction between the two Fourier
coefficients remain. There is no new whole-prefix or closing claim.

## 5. A smaller exact physical rectangle

The two deletions give a concrete reduced finite source. Put
\[
 L_N=\lceil99N/100\rceil,\qquad M_N=\lceil24N/25\rceil,
\]
and denote the literal summand of (11) by \(A_{a,b,N}(w,Z)\).
Define
\[
 \mathcal C_{\beta,N}(w,Z)
      =\sum_{0\le a<L_N}\sum_{0\le b<M_N}A_{a,b,N}(w,Z),
 \qquad
 \mathcal I_{\beta,N}(w,Z)
      =\sum_{a=L_N}^{D}\sum_{b=M_N}^{D}A_{a,b,N}(w,Z).
                                                               \tag{22}
\]
The exact identity is
\[
 \mathcal F_{\beta,N}
     =\mathcal C_{\beta,N}+\mathcal R_{\beta,N}
                +\widetilde{\mathcal E}_{\beta,N}
                -\mathcal I_{\beta,N}.                \tag{23}
\]
Here \(\widetilde{\mathcal E}_{\beta,N}\) is exactly the last
four-percent second-coordinate sector of
[the earlier physical-end theorem, equation (26)](research_mixed_three_four_next_physical_end_sector.md).
Its first-coordinate sum is kept coherent through (10).
The intersection \(\mathcal I_{\beta,N}\) has the positive bound
(20), since it is a subset of that theorem's termwise rectangle.
It is not estimated by subtracting moduli.

Both errors in (23), and the intersection correction, therefore
have ceiling \(7/4\). Their sum satisfies the same ceiling with a
larger polynomial prefactor. On the common smaller neighborhoods
of the actual next ordinary and terminal output families,
\[
 \left|\partial_w^j\partial_z^k
  \left[e^{-N\mathcal P_\beta^+(w,z)}
       \{\mathcal F_{\beta,N}(w,e^{-2\pi iz})
                     -\mathcal C_{\beta,N}(w,e^{-2\pi iz})\}
  \right]\right|
      \le C_{j,k}N^{A_{j,k}}e^{-N/32}.                 \tag{24}
\]
Every retained and deleted sum is an exact polynomial in the
ordinary color and outgoing variable. The comparison is also
valid for all real ordinary colors relative to the complete-color
action, with their fixed Markov derivative bounds.

Thus the entire next source can be reduced, with a calibrated
error, to the displayed smaller physical rectangle. This is a
reduction of the combined two-sector source. It does not assign
the error separately to either Fourier coefficient, nor identify
the partial physical rectangle with the corresponding continuous
rectangle. A later contour representation of \(\mathcal C_{\beta,N}\)
must retain its own sampling kernels, boundary currents and aliases.
