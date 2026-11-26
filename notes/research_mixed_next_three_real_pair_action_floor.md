# Stronger pair estimates for the next power three

Research deduction, 8 November 2026. We improve the geometric action
lower bounds at ordinary and terminal next-three references. The
ordinary case uses a square containing its real coordinates. The
terminal case uses two overlapping rectangles and gives a stronger
bound. All height terms, primitives and source normalizations remain
those of the existing local contribution theorem.

These are action estimates, not lower bounds for the complete
quantum sum. No numerical evaluation is used.

## 1. Two real pair bounds

Use \(J\) and \(B(x,z)=J(x+z)-J(x)-J(z)\) from
[the next-four pair estimate](research_mixed_next_four_real_pair_action_floor.md).
Its Hessian calculation proves strict concavity whenever
\(0<x,z<1/2\). Its elementary integral bounds give
\[
 -J(6/25)>\frac{79}{576},\qquad
 -J(1/3)>\frac{13}{144},\qquad
 \log(2\sin\pi t)>\frac47\quad(9/25\le t\le1/2).
 \tag{1}
\]
As there, \(J(1-t)=-J(t)\) and \(J(1/2)=0\).

**Lemma 1.** On \([6/25,433/1000]^2\),
\[
                            B(x,z)>\frac9{40}.
 \tag{2}
\]

By concavity and symmetry it suffices to check three corners.
The lower-lower corner exceeds \(1/4\), by the cited lemma.
At the mixed corner, the sum is \(673/1000\), whose complement
\(327/1000\) is below \(1/3\) and above \(1/6\).
Thus, even omitting the positive term \(-J(433/1000)\),
\[
 B(6/25,433/1000)>
       \frac{79}{576}+\frac{13}{144}
       =\frac{131}{576}>\frac9{40}.
 \tag{3}
\]
The last difference is \(7/2880>0\).

At the upper-upper corner put \(t=67/500=134/1000\).
For every \(t\in(0,1/2)\), the inequality
\(2\sin(\pi u)\le2\pi u\) gives
\[
                         -J(t)\ge t\{1-\log(2\pi t)\}.
 \tag{4}
\]
Here \(2\pi t<17/20\), since \(\pi<22/7\), and
\(\log(17/20)<-3/20\). Hence
\[
 -J(67/500)>\frac{1541}{10000},\qquad
 -2J(433/1000)>\frac{67}{875}.
 \tag{5}
\]
The second inequality is the last integral bound in (1).
Reflection now yields
\[
 B(433/1000,433/1000)>
 \frac{1541}{10000}+\frac{67}{875}
       =\frac9{40}+\frac{397}{70000}>\frac9{40}.
 \tag{6}
\]
This proves the lemma.

**Lemma 2.** On
\([6/25,2/5]\times[6/25,11/25]\), and on its transpose,
\[
                               B(x,z)>\frac14.
 \tag{7}
\]

Again consider the four corners. The lower-lower corner is
already covered. At \((6/25,11/25)\), reflection at the summed
coordinate gives \(-J(8/25)>13/144\), while
\(-J(11/25)>6/175\). Therefore
\[
 B(6/25,11/25)>
              \frac{131}{576}+\frac6{175}>\frac14.
 \tag{8}
\]
The last difference is \(1181/100800>0\).
At \((2/5,6/25)\), the complement of the sum is \(9/25\).
The last inequality in (1) gives
\[
 B(2/5,6/25)>
 \frac{79}{576}+\frac2{35}+\frac2{25}
       =\frac{79}{576}+\frac{24}{175}>\frac14.
 \tag{9}
\]

At the upper-upper corner the complementary summed argument is
\(4/25\). Since
\[
           2\pi(4/25)<\frac{176}{175},\qquad
           \log(176/175)<\frac1{175},
\]
(4) gives \(-J(4/25)>696/4375\). Thus
\[
 B(2/5,11/25)>
 \frac{696}{4375}+\frac2{35}+\frac6{175}
       =\frac{1096}{4375}
       =\frac14+\frac9{17500}>\frac14.
 \tag{10}
\]
Concavity proves (7). The smallest displayed margin is positive;
no claim about the location of an interior minimum is needed.

## 2. Application to the unchanged geometric action

Let \(y=t_2,s=s_3,z=t_3\) be the original matched coordinates,
with \(y=q_{34}(s)\). Set \(x_v=\Re v\), \(h_v=\Im v\), and
\(\chi=117/(800\pi)>9/200\). The exact next-three identity is
\[
 \mathcal P_0^+(-2,z)-\mathcal P_{34}(-2,y)
       =W(y,s)+W(s,z)-g(y)-2\pi isz,
 \qquad \Re\mathcal P_{34}(-2,y)>\frac74 .
 \tag{11}
\]
The identity and the original vertical-convexity argument are
recorded in
[the physical end-sector theorem, Section 3](research_mixed_three_four_next_physical_end_sector.md).
The retained incoming factorial term satisfies
\(-\Re g(y)>\chi\), by
[the kernel-margin theorem, Section 3](research_mixed_next_low_index_kernel_margin.md).
In particular replacing a real pair lower bound \(b\) in that
argument gives the complex bound
\[
                \Re W(v,w)>b-\pi(x_vh_w+x_wh_v).
 \tag{12}
\]
All relevant pairs lie in the same established height rectangle,
so only the real pair constants are improved.

For an ordinary next three the real coordinates of both pairs
lie in the square of Lemma 1. Its two bounds improve the earlier
sum \(2/5\) to \(9/20\), an increase of \(1/20\).
The signed height estimates in
[the binomial end theorem, Section 5](research_mixed_three_four_next_binomial_end_bound.md)
therefore give
\[
           \Re\mathcal P_0^+(-2,z)>\frac{41}{20}+\chi
                                             >\frac{419}{200}.
 \tag{13}
\]

When the actual ordinary output has \(h_z\ge0\), retain its
favorable height term as in
[the all-output seam corollary](research_mixed_next_all_typed_seam_collar.md).
Explicitly \(h_y<0\), \(x_s>0\), and the actual ranges give
\[
 x_s(h_z-h_y)>0,\qquad
 h_s(x_z-x_y)\ge-\frac{12545}{10^6},\qquad
              \frac{12545\pi}{10^6}<\frac1{25}.
 \tag{14}
\]
Equations (11)--(12) then give the stronger bound
\[
 \Re\mathcal P_0^+(-2,z)>
 \frac74+\frac9{20}+\frac9{200}-\frac1{25}
       =\frac{441}{200},\qquad h_z\ge0.
 \tag{15}
\]
This sign condition is imposed only on the reference point.
The resulting strict margin persists on a small complex
neighborhood without imposing a sign on its nearby points.

For a terminal next three the real coordinate ranges are
\[
 x_y\in[.24,.36],\qquad
 x_s\in[.278,.391],\qquad
 x_z\in[.376,.438].
 \tag{16}
\]
Both \((x_y,x_s)\) and \((x_s,x_z)\) lie in the rectangle of
Lemma 2. Thus the earlier pair sum gains \(1/10\).
Keeping the existing terminal signed-height estimate unchanged
gives
\[
             \Re\mathcal P_0^+(-2,z)>
                     \frac{109}{50}+\chi>\frac{89}{40}.
 \tag{17}
\]

**Theorem 3.** The bounds (13), (15), and (17) hold for the
original conditional action on their stated actual reference
families. They retain the original constants and logarithmic
branches. Compactness supplies fixed sufficiently small
complete-color and actual-output neighborhoods for each strict
weaker lower bound.

These larger geometric allowances can be compared with bounds
for the full finite source. They do not by themselves suppress
either Fourier coefficient or establish a knot volume identity.
