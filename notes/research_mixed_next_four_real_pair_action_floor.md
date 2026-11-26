# A stronger action lower bound for the next power four

Research deduction, 8 November 2026. The real coordinates of the
actual next-four references occupy a smaller interval than the
rectangle used for the previous pair estimate. Keeping this interval
improves the lower bound for each of the two real pair actions from
\(1/5\) to \(1/4\). The resulting conditional action gains \(1/10\).
This is a bound for the action of the geometric critical point,
not a lower bound for the complete finite sum.

No numerical evaluation or change to a frozen proof is used.

## 1. A real pair inequality

Let
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 B(x,z)=J(x+z)-J(x)-J(z).
 \tag{1}
\]
All arguments below lie in \((0,1)\). Set
\[
                         a=\frac6{25},\qquad b=\frac{91}{250}.
 \tag{2}
\]

**Lemma 1.** For every \(x,z\in[a,b]\),
\[
                              B(x,z)>\frac14.
 \tag{3}
\]

To prove this, first observe that \(B\) is strictly concave on
the rectangle. If \(A=\cot(\pi x)\), \(D=\cot(\pi z)\), and
\(C=\cot(\pi(x+z))\), its Hessian divided by \(\pi\) is
\[
 \begin{pmatrix}C-A&C\\ C&C-D\end{pmatrix}.
 \tag{4}
\]
Here \(A,D>0\), \(C=(AD-1)/(A+D)\), and
\[
             C-A=-\frac{A^2+1}{A+D}<0,\qquad
             (C-A)(C-D)-C^2=1.
 \tag{5}
\]
Thus (4) is negative definite. Concavity reduces the lower bound
to the four corners; symmetry leaves three cases.

We give explicit integral bounds for these corners. The identities
\(J(1/2)=0\) and \(J(1-t)=-J(t)\) follow from the usual sine
integral and reflection. On \([1/4,1/2]\) the function
\(\log(2\sin\pi t)\) is concave. Its integral on each interval
is therefore at least the area under its endpoint chord. Use
\[
 \log\sqrt2>\frac13,\qquad
 \log\sqrt3>\frac{13}{24},\qquad
 \frac23<\log2<\frac7{10}.
 \tag{6}
\]
For the lower bounds, the positive series
\(\log v=2\sum_{k\ge0}((v-1)/(v+1))^{2k+1}/(2k+1)\)
at \(v=2,3\) suffices. For the upper bound,
\(1+7/10+49/200+343/6000>2\).
The two chords on \([1/4,1/3]\) and \([1/3,1/2]\) give
\[
 -J(a)>-J(1/4)>
 \frac1{24}\left(\frac13+\frac{13}{24}\right)
 +\frac1{12}\left(\frac{13}{24}+\frac23\right)
 =\frac{79}{576}.
 \tag{7}
\]
The first inequality uses positivity of the integrand between
\(a\) and \(1/4\). Also
\[
                     J(2a)>-\frac1{50}\log2>-\frac7{500}.
 \tag{8}
\]
Hence
\[
 B(a,a)>\frac{79}{288}-\frac7{500}
            =\frac14+\frac{371}{36000}>\frac14 .
 \tag{9}
\]

For \(9/25\le t\le1/2\), monotonicity of sine and
\(\pi<22/7\) give
\[
 \sin(\pi t)\ge\cos(7\pi/50)>
 1-\frac12\left(\frac{11}{25}\right)^2>\frac9{10}.
 \tag{10}
\]
The logarithm series, or its first term, gives
\(\log(9/5)>4/7\). Therefore
\[
 -J(b)>\left(\frac12-b\right)\frac47=\frac{68}{875},
 \qquad
 -J(1-a-b)>
       \left(\frac12-(1-a-b)\right)\frac47=\frac{52}{875}.
 \tag{11}
\]
Here \(1-a-b=99/250>9/25\). Reflection and (7), (11) imply
\[
 B(a,b)>
 \frac{79}{576}+\frac{120}{875}
 =\frac{79}{576}+\frac{24}{175}>\frac14 .
 \tag{12}
\]
For example the difference in the last inequality is
\(2449/100800>0\).

Finally \(1-2b=34/125<3/10\). The integrand is positive from
\(34/125\) to \(1/2\); on \([3/10,1/3]\) it exceeds \(1/3\),
and on \([1/3,1/2]\) it exceeds \(13/24\). Consequently
\[
 -J(1-2b)>
                  \frac1{90}+\frac{13}{144}=\frac{73}{720}.
 \tag{13}
\]
Using (11) once more gives
\[
 B(b,b)>
 \frac{73}{720}+\frac{136}{875}
       =\frac14+\frac{859}{126000}>\frac14.
 \tag{14}
\]
This proves all three corner estimates and the lemma.

## 2. Retain the original complex action and height terms

Use the actual coordinates \(y=t_2,s=s_3,z=t_3\), with
\(y=q_{34}(s)\), and the original primitives
\[
 g(v)=J(v)+\frac{i\pi}{2}(v-v^2),\qquad
 W(v,w)=J(v+w)-J(v)-J(w)+i\pi vw .
 \tag{15}
\]
Write \(x_v=\Re v\), \(h_v=\Im v\). The
[physical end-sector theorem, equations (16)--(22)](research_mixed_three_four_next_physical_end_sector.md)
gives the exact identity
\[
 \mathcal P_1^+(-2,z)-\mathcal P_{34}(-2,y)
       =W(y,s)+W(s,z)-g(y)-g(s)-2\pi isz,
 \qquad \Re\mathcal P_{34}(-2,y)>\frac74 .
 \tag{16}
\]
The vertical convexity argument in
[terminal transform tails, Lemma 1](research_mixed_terminal_transform_tails.md)
applies on \([.23,.45]+i[-.12,.12]\).
Replacing only its real-height pair lower bound by Lemma 1 yields
\[
 \Re W(v,w)>
       \frac14-\pi(x_vh_w+x_wh_v)
 \tag{17}
\]
whenever both real coordinates lie in \([a,b]\) and the original
height ranges hold. Its linear height terms and logarithmic branches
are unchanged.

All three real coordinates of an actual ordinary next-four
reference belong to \([.24,.36]\). For a terminal next four the
respective intervals for \(y,s,z\) are
\([.24,.36]\), \([.246,.350]\), and \([.333,.363]\).
They all lie in \([a,b]\). These are precisely the typed ranges
in [the binomial end theorem, Section 5](research_mixed_three_four_next_binomial_end_bound.md).
Both pairs in (16) therefore satisfy (17).

The same source gives the bounds
\[
 h_s(x_z-x_y)+x_s(h_z-h_y)\ge
 \begin{cases}
 -48600/10^6,&\text{ordinary next four},\\
 -30784/10^6,&\text{terminal next four}.
 \end{cases}
 \tag{18}
\]
These follow directly from its signed coordinate intervals;
no independent-coordinate optimization replaces the actual reference.
The [kernel-margin theorem, Section 3](research_mixed_next_low_index_kernel_margin.md)
retains both factorial contributions:
\[
 -\Re g(y)>\chi,\qquad-\Re g(s)>\chi,\qquad
                  \chi=\frac{117}{800\pi}>\frac9{200}.
 \tag{19}
\]
Combining (16)--(19) gives
\[
 \Re\mathcal P_1^+(-2,z)>
 \frac94+2\chi-
 \begin{cases}
 (48600/10^6)\pi,&\text{ordinary next four},\\
 (30784/10^6)\pi,&\text{terminal next four}.
 \end{cases}
 \tag{20}
\]
Since \(\pi<22/7\), the two losses are less than \(4/25\)
and \(1/10\), respectively. We obtain:

**Theorem 2.** On every actual reference in the indicated family,
with the original conditional normalization,
\[
 \boxed{\quad
 \Re\mathcal P_1^+(-2,z)>
 \begin{cases}
 209/100+2\chi>109/50,&\text{ordinary next four},\\
 43/20+2\chi>56/25,&\text{terminal next four}.
 \end{cases}
 \quad}
 \tag{21}
\]
The improvement over the earlier typed floors is exactly \(1/10\).
The strict inequalities persist on fixed sufficiently small
complete-color and actual-output neighborhoods by continuity and
compactness of the reference families. This does not extend the
reference domain to an independent complex box.

The theorem supplies a larger allowance for estimates of competing
finite-source contributions. Proving that those contributions are
small still requires their own bounds; the action estimate alone
does not prove a nonzero coefficient in the complete quantum sum.
