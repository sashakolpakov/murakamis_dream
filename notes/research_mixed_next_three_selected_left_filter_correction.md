# The original filter correction on the selected left interval

Private research proof candidate, 8 November 2026. A sharper
endpoint comparison pays the complete old filter correction on
the upper-left contour. Its growth outside the unit disk is
included explicitly. The proof does not alter the old filter or
infer a bound for the full first factor from a correction bound.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. A stronger preceding-factor allowance

Retain the actual references, domain, phases, and finite kernels of
[selected-left bounded-prefix attachment](research_mixed_next_three_selected_left_bounded_prefix.md).
Thus the word begins \(343\), has length at least five,
\(y=q+i/100\), \(0\le q\le11/50\), and the outgoing real
coordinate lies in \([3/10,39/100]\), with its actual fixed
height. Write
\[
 B_0=2383/1500,\qquad R=e^{\pi/50},\qquad
 B_f=77/50+\pi/50 .
 \tag{1}
\]

**Theorem 1.** Suppose that a preceding factor, independent of
the next private index, satisfies
\[
                  |V_N|\le CN^a e^{NB_f}.
 \tag{2}
\]
Then, at both parities and uniformly on the stated actual domain,
\[
 |V_Nd_N(Y)Y^{-N}C_{0,N}(Y,Z)|
          \le C' N^{a'}e^{N\{\Lambda_{123}(z)-1/2000\}} .
 \tag{3}
\]

Here \(d_N\) is still the entire original forced polynomial.
The two selected weight rates are
\[
 W_{\rm fac}=-\Re g(y)-2\pi/100,\qquad W_{\rm force}=0 .
 \tag{4}
\]
They are bounded separately; neither replaces the other.

## 2. The improved endpoint reserve

Set \(q_0=11/50\), \(c=\Im t_2^*<0\).
The original negative-height calibration, equation (9) of
the preceding note, has reserve \(1/50\) against \(B_0\).
All subsequent q-transport, physical-row, and finite-current
arguments of that note are unchanged. Only its selected
endpoint comparison is strengthened here.

First,
\[
 e^{9/25}>1+\frac9{25}+\frac{81}{1250}+\frac{729}{93750}
           =\frac{134304}{93750}>\frac{10}{7},
 \qquad -c<\frac9{50\pi}.
 \tag{5}
\]
The last inequality uses the actual shared-radius lower bound.
For a clipped main index with real part at least \(1/6\),
the same argument bounds as equations (12)--(13) of the
preceding note now give a factorial-branch increase at most
\[
       \frac{17\pi}{75}\frac9{50\pi}
                    -\frac{91}{2500}
         =\frac{11}{2500}.
 \tag{6}
\]
The main factorial reserve is therefore greater than
\[
                         \frac1{50}-\frac{11}{2500}
                              =\frac{39}{2500}.
 \tag{7}
\]

The forcing branch has a better comparison than the bound
obtained by discarding the sign of \(g(q_0+ic)\). Its exact
dilogarithm integral, equation (22) of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md),
gives
\[
 -\Re g(q_0+ic)
 \ge \frac{\sin(2\pi q_0)}{2\pi}
                              \log(1+e^{2\pi c})
 >\frac3{20\pi}.
 \tag{8}
\]
Indeed \(\sin(2\pi q_0)>3/4\),
\(e^{2\pi c}>7/10>1/2\), and
\(\log(3/2)>2/5\).
To obtain the first inequality directly, use
\[
 \arg(1-se^{-i\theta})
 \ge\frac{s\sin\theta}{|1-se^{-i\theta}|}
 \ge\frac{s\sin\theta}{1+s},\qquad 0<s<1,\quad0<\theta<\pi,
 \]
and integrate after division by \(s\).
The argument is in \((0,\pi/2)\), so the first inequality
uses \(\alpha\ge\sin\alpha\) there.

The positive-height increase of the bare phase is at most
\(13\pi/5000\); the negative-height increase is nonpositive,
as proved in (17) of the preceding note. Since
\[
                    \frac3{20\pi}>\frac{13\pi}{5000}
 \tag{9}
\]
(even \(\pi<4\) suffices), adding \(\Re g(q_0+ic)\)
makes the complete forcing-branch change strictly negative.
Its endpoint reserve is consequently still \(1/50\).

For the real low cut, use
[the selected type-three low-cut comparison, Theorem 1](research_mixed_selected_three_left_rows.md)
at \(q=q_0\), \(H=1/100\). Its hypotheses contain the present
actual output and private heights. It bounds the real cut
\(t=3/20\) by the main profile at \(11/50+ih_t\), with
an additional gap \(1/125\). The selected weight is independent
of the private index, so the statement applies to both branches.
Equation (7) therefore leaves reserve greater than
\(39/2500+1/125\) for this cut. The monotone q-transport
of that cut in the preceding note retains it on the whole
left interval.

The real half cut retains reserve \(7/400\), and the last
profile retains \(1/50\), exactly as before. Thus every
required main, real-cut, or last profile, paired with either
selected weight and \(B_0\), has reserve greater than
\(39/2500\). The prefix-independent upper-row comparison
retains this same reserve for every physical upper row.

## 3. Complete finite attachment at the larger rate

The additional preceding rate in (1) is strictly less than
\[
 B_f-B_0=\frac{\pi}{50}-\frac{73}{1500}
          <\frac{149}{10500}.
 \tag{10}
\]
Consequently the common profile reserve after attaching (2)
is greater than
\[
              \frac{39}{2500}-\frac{149}{10500}
                   =\frac{37}{26250}>\frac1{1000}.
 \tag{11}
\]

Use the complete finite assembly in Sections 4--6 of the
preceding note: the physical low block, every physical upper
row, the main integral with coefficient \(+N\), two horizontal
aliases, four weighted sides, and two unweighted joins.
Both selected terms of \(d_N\) remain. All underlying
phase comparisons are independent of the constant preceding
rate, so increasing that constant only subtracts (10) from
their reserves.

Choose the total factorial, finite-product, and half-grid
tolerances, followed by the elementary Laurent-polynomial
extension to \(q=0\), to cost less than half the reserve
in (11). The fixed polynomial factors remain polynomial,
and
\[
                        \frac{37}{52500}>\frac1{2000}.
 \tag{12}
\]
This proves (3) for the original complete finite kernel.

## 4. Application to the unchanged filter

Let
\[
 E_N^{\rm filt}(w,Y)=F_N(w,Y)-F_N^{\rm mid}(w,Y)
 \tag{13}
\]
be exactly the correction in Section 4 of
[the actual lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md).
It includes both the original first-node deletion and the old
cardinal projection. Its degree in \(Y\) is at most \(D=N-1\),
and that source proves
\[
 \sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
       \le CN^a e^{77N/50},\qquad -2\le w\le2 .
 \tag{14}
\]
The reciprocal-polynomial maximum principle, applied before
any further multiplication, gives
\[
 |E_N^{\rm filt}(w,Y)|
       \le CN^a e^{77N/50}R^D
       \le CN^a e^{NB_f}\qquad(|Y|=R).
 \tag{15}
\]
Theorem 1 applies to this complete correction. In particular
its two original parts need not satisfy separate coefficient
bounds in this application.

On the top contour define the unfiltered and old filtered
meromorphic expressions
\[
 K_N^{\rm full}(y)=
       \frac{N F_N(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},
 \qquad
 K_N(y)=
       \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N}.
 \tag{16}
\]
Their exact difference is
\[
 K_N^{\rm full}-K_N
       =-\frac{N E_N^{\rm filt}(w,Y)d_N(Y)Y^{-N}
                              C_{0,N}(Y,Z)}{1-Y^{-N}} .
 \tag{17}
\]
Since \(|Y|=R>1\), the denominator in (17) is bounded
below by \(1/2\) for all sufficiently large \(N\).
Equations (3) and (15) prove a pointwise exponentially
smaller bound for (17) throughout \(0\le q\le11/50\).
No boundary pole is crossed: this identity is only used
on the fixed positive-height contour.

The numerator in (17) is polynomial of degree at most \(D\)
in each of \(w,Z\). Apply
[horizontal complex extension](research_mixed_horizontal_complex_extension.md)
to the real color interval and the outgoing arc in (2),
then compare at the fixed actual reference using
\(\Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*)\).
Shrinking the outside neighborhoods and applying Cauchy's
formula gives, for every fixed \(j,k\),
\[
 \partial_w^j\partial_z^k
 \left[
 e^{-N\mathcal P_0^+(w,z)}
 \int_{[0,\,11/50]+i/100}
          (K_N^{\rm full}-K_N)(y)\,dy
 \right]=O_{j,k}(e^{-N/10000}) .
 \tag{18}
\]
The same conclusion holds on every fixed subinterval.
All references, heights, cutoffs and paths remain fixed when
these outside derivatives are taken.

This pays the original filter correction on the selected
left interval. It does not pay \(K_N^{\rm full}\) there:
the remaining first-factor contributions still require
their own bounds. No noncancellation or short-filling
stability theorem follows from (18) alone.
