# Extending the own-three upper band at a fixed shared coordinate

Private research proof, 8 November 2026. A further part of the next
own-three positive upper block can be moved into the already bounded
band without changing the shared coordinate. The exact reflected
row derivative is uniformly positive when the reflected index is at
least \(3/10\) and lies less than \(1/5\) beyond that coordinate.
This gives a complete finite estimate with the original first factor.

No numerical evaluation or modification of a frozen input is used.
The remaining smaller reflected indices and the noncentral first
incoming paths are not estimated here.

## 1. Source and exact finite conclusion

Use precisely the ordinary-next own-three references, original cap
plane, following plane \(\Lambda_{123}(z)\), and allocations in
[the enlarged-band theorem](research_mixed_next_own_three_upper_band_old_face.md).
In particular
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.065<h_z<.068,\\
X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad Z=e^{-2\pi iz},
\qquad 13/25<R<1,\quad |Z|<43/28 .
\end{gathered}                                                    \tag{1}
\]
All geometric-reference correlations remain imposed. Let
\(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), and \(p_j(W)=(rW;r)_j\). Put
\[
\begin{split}
b(q)&=\max\{7/10,4/5-q\},\\
\mathcal U_{0,N}^{\,b}(Y,Z;q)
 &=\sum_{\lceil N/2\rceil\le j\le\lfloor Nb(q)\rfloor}
       \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|.
\end{split}                                                       \tag{2}
\]
The first kernel \(C_{1,N}(X,Y)\) and the cap \(U_{0,N}(w,X)\)
are complete. The forced shared weight is the original \(d_N(Y)\).
There is no outgoing halfweight for the next own-three factor.

**Theorem.** For every real ordinary color and all sufficiently large
integer levels of both parities,
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|\,
       \mathcal U_{0,N}^{\,b}(Y,Z;q)
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
\quad}                                                           \tag{3}
\]
Arbitrary subsets of the positive sum have the same bound. Combining
(3) with [the complete-first below-half theorem](research_mixed_next_own_three_below_half_complete_first.md)
also bounds the literal signed next truncation
\[
\sum_{j=0}^{\lfloor Nb(q)\rfloor}
               \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}                 \tag{4}
\]
with the complete first factor and shared weight as in (3).
The actual central first incoming integral retains its original
measure \(+N\,da\). Fixed-base signed sums and that integral have
normalized local mixed jets with gap \(10^{-12}\), with the same
outside-variable conventions as the two input theorems.
The integer index sets are frozen before those derivatives are taken.

## 2. The original reflected derivative

Keep the full physical rate, including the incoming chirp,
\[
E_0(t;y,z)=
\int_0^t\log|1-e^{-2\pi i(y+s)}|\,ds+
\int_0^t\log|1-e^{-2\pi i(z+s)}|\,ds
-2J(t)-2\pi h_y t.                                           \tag{5}
\]
For \(v=1-t\) and \(T=R^{-1}\), direct differentiation gives
\[
\frac{d}{dv}E_0(1-v;y,z)
=\log\frac{\{2\sin(\pi v)\}^2}
 {|T-e^{2\pi i(v-q)}|\,|1-Ze^{2\pi iv}|}.                     \tag{6}
\]
For example, the incoming modulus before folding is
\(|1-R e^{2\pi i(v-q)}|\). The chirp contributes \(\log R\),
which changes that modulus to the first denominator in (6).
Thus (6) preserves the original carrier rather than dropping
the radial drift. Every outgoing logarithmic zero is retained;
the derivative then has an integrable positive singularity.

Suppose
\[
3/10\le v\le q+1/5,\qquad 0\le q\le11/50.                    \tag{7}
\]
This implies \(0<v-q\le1/5\) and \(v\le21/50<1/2\).
The correlated outgoing-modulus inequality in Section 3,
equation (14), of the enlarged-band theorem gives
\[
\frac{\{2\sin(\pi v)\}^2}{|1-Ze^{2\pi iv}|}>2.               \tag{8}
\]
Its proof covers the full independent \(u\in P\), both
outgoing-height signs, and the whole radius interval
\(0\le|Z|\le43/28\).

The other factor in (6) is strictly less than two. Indeed
\[
\cos(2\pi(v-q))\ge\cos(2\pi/5)>3/10,
\qquad 1<T<25/13.
\]
The cosine inequality follows from
\(\cos(2\pi/5)=(\sqrt5-1)/4\) and \(\sqrt5>11/5\).
The squared modulus increases with \(T\ge1\), so
\[
|T-e^{2\pi i(v-q)}|^2
<1+(25/13)^2-\frac35\frac{25}{13}
=\frac{599}{169}<4.                                        \tag{9}
\]
Equations (6)--(9) give the uniform strict bound
\[
\frac{d}{dv}E_0(1-v;y,z)
>\log\frac{26}{\sqrt{599}}
>\frac{77}{1352}>\frac1{20}.                                \tag{10}
\]
Here \(\log(1+\xi)>\xi/(1+\xi)\) for \(\xi>0\), applied
to \(676/599=1+77/599\), proves the middle inequality.
The comparison integrates through the possible zeros just described.
Consequently
\[
E_0(1-v;y,z)
\le E_0(4/5-q;y,z)-\frac{q+1/5-v}{20}
\quad\hbox{on (7)}.                                        \tag{11}
\]
The right endpoint \(v=q+1/5\) is the exact continuous
boundary of the previously bounded band.

## 3. Complete finite source at that boundary

The enlarged-band proof supplies more than a bound on a coherent
sum. Its equations (24) and (30) bound, with deficit \(10^{-10}\),
the joint rate at every continuous \(v-q\ge1/5\), for each
controlling first main, real-low, real-half and last profile.
Its complete cap plane and the full shared allocation are retained.
In particular those statements apply at the exact endpoint
\(v=q+1/5\), whether or not \(N(4/5-q)\) is an integer.

All preceding factors and their profiles are independent of \(v\).
Thus (11) bounds each same-point joint profile in (7) by its
already bounded endpoint profile. No finite physical value at a
nonintegral index is substituted: the comparison is first between
continuous physical rates.

For an actual row \(j\), take \(v=1-j/N\). The zero-safe uniform
factorial and numerator-product bounds used in the enlarged-band
proof bound its literal modulus by (5) with polynomial prefactors
and arbitrarily small prescribed rate tolerances. The new rows
remain in a compact physical-index interval away from zero and one.
All outgoing zeros and the exact incoming power \(Y^{-j}\) remain.

The first low positive block is reduced to its real cut. Its
complete middle interpolation retains both horizontal aliases,
all four weighted vertical halves and both unweighted joins.
The first positive upper block retains its real-half and last
alternatives. These are exactly the same first-factor groups in
Section 6 of the enlarged-band theorem; multiplying by a next
physical row does not alter their comparisons. Equation (11)
pays every resulting profile in the additional range (7).
Choose the finite-product tolerances within the \(10^{-10}\)
profile reserve and sum the positive next rows. This costs only
a polynomial and proves (3).

When \(q\le1/10\), (2) is the old band and there are no new rows.
When \(q>1/10\), its additional rows have
\(3/10\le v<q+1/5\), precisely (7). This verifies the stated
floor cutoff without an unaccounted endpoint row.
The first and next half-index conventions remain unchanged
at both parities. Adding the signed below-half source proves (4).

The same uniform upper-rate argument holds with its fixed index
sets on small outside-parameter neighborhoods, after reserving a
smaller loss, by the original all-real color polynomial and
logarithmic-arc polynomial continuation. The shared coordinate
and base references are fixed labels in this argument. The
ordinary normalization is the same nonzero local next action.
Cauchy's formula therefore gives the stated normalized jets.
Neither derivatives of an absolute sum nor derivatives of a moving
floor function are asserted.

## 4. Remaining part of the middle strip

The new estimate reduces the unresolved strip \(q<v<q+1/5\) to
\[
q<v<\min\{3/10,q+1/5\}.                                    \tag{12}
\]
It does not estimate \(v\le q\), a last-row alternative, or
the remainder of the coherent next kernel. The noncentral first
incoming paths and the other Fourier contours remain separate.
In particular (3) is a central partial-source estimate, not a
complete next-transfer or arbitrary short-composition theorem.
