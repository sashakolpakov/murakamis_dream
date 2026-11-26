# A larger own-three upper end at deeper shared heights

Private research proof, 8 November 2026. At shared radius
\(|Y|\le7/10\), every next own-three row with reflected index
at most \(11/50\) is bounded by its original last-row rate,
independently of the shared real coordinate in \([0,11/50]\).
The already proved complete-first last-profile comparison then
pays this positive finite block.

Together with the enlarged band, this proves a complete central
first-factor estimate for the next own-three kernel on
\(0\le\Re y\le1/50\) at these deeper heights. The other shared
coordinates, shallower heights and noncentral first incoming
paths remain separate. No numerical evaluation or frozen-source
edit is used.

## 1. Original source and the reflected rate

Keep the actual ordinary-next own-three references, planes and
finite factors of
[the upper-end theorem](research_mixed_next_own_three_upper_end_last_reduction.md).
Thus
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.065<h_z<.068,\\
X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad
Z=\rho e^{-2\pi iu},\qquad 13/25<R\le7/10 .
\end{gathered}                                                   \tag{1}
\]
Every actual reference correlation remains imposed. Write
\[
L_0=-\log R+\log_+\rho,\qquad T=R^{-1}\ge10/7.
\tag{2}
\]
The original physical rate and its complete-period value are
\[
\begin{split}
E_0(t;y,z)
 &=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
  +\int_0^t\log|1-Ze^{-2\pi ib}|\,db
       -2J(t)-2\pi h_y t,\\
E_0(1;y,z)&=L_0 .
\end{split}                                                     \tag{3}
\]
In particular a positive outgoing height contributes
\(\log_+\rho=2\pi(h_z)_+\); it is not discarded.

For \(v=1-t\), the exact reflected identity from Section 1
of the upper-end theorem is
\[
\begin{split}
\Phi(v)&:=E_0(1-v;y,z)-L_0\\
 &=2J(v)
 -\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
 -\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds .
\end{split}                                                     \tag{4}
\]
Both original carriers are included in (2)--(4).
All integrable logarithmic zeros keep their original limits.

## 2. Centering the incoming arc

Suppose \(0\le v\le11/50\). The first integrand in (4) is
even, increases with distance from zero on \([0,1/2]\),
and increases with \(T\ge1\). Its arc lies in
\([-11/50,11/50]\). Among arcs of this fixed length its
integral is minimized by centering at zero. Consequently
\[
\begin{split}
\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
&\ge\int_{-v/2}^{v/2}\log|T-e^{2\pi is}|\,ds\\
&=\int_0^v\log|T-e^{\pi is}|\,ds\\
&\ge\int_0^v\log|10/7-e^{\pi is}|\,ds .
\end{split}                                                     \tag{5}
\]
For a direct verification of the centering step, differentiate
the integral with respect to its center. Its derivative is
the difference of the two endpoint values, with the sign
of that center, by evenness and angular monotonicity.

The outgoing arc lies in \([0,1/2]\), since \(u\ge11/50\ge v\).
The same translation and radial primitive argument as equations
(8)--(9) of the upper-end theorem gives
\[
\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds\ge J(v).
\tag{6}
\]
This holds for \(0<\rho\le1\). For \(\rho>1\), first take out
\(v\log\rho\) and use the reciprocal radius; the resulting
lower bound is even larger. Thus (6) retains both outgoing
height signs.

Set
\[
H(v)=J(v)-\int_0^v\log|10/7-e^{\pi is}|\,ds .
\tag{7}
\]
Equations (4)--(6) give \(\Phi(v)\le H(v)\).

## 3. The centered envelope has no positive value

Put \(T_0=10/7\), \(c=\cos\pi v\), and
\(A(s)=|T_0-e^{\pi is}|\). The derivative of (7) is
\[
H'(v)=\log\frac{2\sin\pi v}{A(v)}.
\tag{8}
\]
Its sign is the sign of
\[
4\sin^2\pi v-A(v)^2
       =3-T_0^2+2T_0c-4c^2.
\tag{9}
\]
On \(0\le v\le11/50\), one has
\[
\pi v<7/10,\qquad c>1-\frac{(7/10)^2}{2}>3/4.
\]
The derivative of (9) with respect to \(c\) is
\(2T_0-8c<0\). Since \(c\) decreases with \(v\),
(9) increases with \(v\). At zero it is
\(-(T_0-1)^2<0\). Therefore \(H'\) can change sign
only from negative to positive. The maximum of \(H\)
on this interval is at zero or at \(11/50\).
This is a sign-change argument, not an assertion that
\(H\) is convex everywhere.

We bound the latter endpoint by four explicit arc pieces.
The function \(A(s)\) increases with \(s\). At the successive
left endpoints \(s=0,11/200,11/100,33/200\), it satisfies
\[
A(0)=3/7,\qquad
A(11/200)>47/100,\qquad
A(11/100)>29/50,\qquad
A(33/200)>37/50 .
\tag{10}
\]
Here are elementary rational witnesses. For
\(0<\theta\le33\pi/200<13/25\),
\[
1-\cos\theta\ge\frac{\theta^2}{2}-\frac{\theta^4}{24}
                   >\frac{12}{25}\theta^2.
\]
Also \(\pi>25/8\), so at the three positive endpoints
\(\theta=\pi s\) exceeds \(11/64,11/32,33/64\), respectively.
Since
\[
A(s)^2=\frac9{49}+\frac{20}{7}(1-\cos\pi s),
\]
the resulting squared lower bounds are
\[
\begin{array}{c|c|c}
s&A(s)^2\text{ lower bound}&\text{comparison}\\ \hline
11/200&14061/62720&(47/100)^2<14061/62720\\
11/100&5421/15680&(29/50)^2<5421/15680\\
33/200&34389/62720&(37/50)^2<34389/62720 .
\end{array}                                                     \tag{11}
\]

The logarithmic bounds needed for (10) are
\[
\log(7/3)<6/7,\quad \log(100/47)<4/5,\quad
\log(50/29)<3/5,\quad \log(50/37)<1/3 .
\tag{12}
\]
They follow from the following positive partial exponential
series, with all comparisons rational:
\[
\begin{split}
e^{6/7}&>5647/2401>7/3,\\
e^{4/5}&>827/375>100/47,\\
e^{3/5}&>227/125>50/29,\\
e^{1/3}&>25/18>50/37 .
\end{split}                                                     \tag{13}
\]
The first line uses terms through degree four, the next
two through degree three, and the last through degree two.

Each of the four arc pieces has length \(11/200\).
Equations (10)--(13) therefore imply
\[
\int_0^{11/50}\log A(s)\,ds
>-\frac{11}{200}\left(\frac67+\frac45+\frac35+\frac13\right)
=-\frac{374}{2625}.
\tag{14}
\]
The already proved sine-integral bound in
[the own-four upper-row theorem, equation (10)](research_mixed_next_lower_left_own_four_upper_rows.md)
is
\[
-J(11/50)>\frac{63}{440}
                 +\frac3{100}\log(5/4)>\frac{989}{6600}.
\tag{15}
\]
It uses the original Catalan lower witness and
\(\log(5/4)>2/9\); no new action value is evaluated here.
Combining (7),(14),(15) gives
\[
H(11/50)<-\frac{989}{6600}+\frac{374}{2625}
                    =-\frac{1703}{231000}<0 .
\tag{16}
\]
Since \(H(0)=0\), the sign-change argument proves \(H(v)\le0\)
on the whole interval. In particular
\[
\boxed{\quad E_0(1-v;y,z)\le L_0
 \qquad(0\le v\le11/50,\quad 0\le q\le11/50,\quad R\le7/10).
\quad}                                                         \tag{17}
\]
This is a rate comparison with the actual last alternative,
not a division by the terminal finite row.

## 4. The positive finite block and complete first factor

For \(r=e^{-2\pi i/N}\), \(D=N-1\),
\(P_j=(r;r)_j\), and \(p_j(W)=(rW;r)_j\), define
\[
\mathcal U_{0,N}^{\,78}(Y,Z)
=\sum_{\lceil39N/50\rceil\le j\le D}
       \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|.
\tag{18}
\]
Every actual row here has \(v=1-j/N\le11/50\).
The original zero-safe numerator and endpoint-uniform factorial
bounds, including \(j=D\) and both parities, give for every
prescribed \(\tau>0\)
\[
\mathcal U_{0,N}^{\,78}(Y,Z)
 \le C_\tau N^{B_\tau}e^{N(L_0+\tau)}.
\tag{19}
\]
This retains the whole positive row sum. In particular a zero
in \(p_D(Z)\) causes no factorization or cancellation problem.

Sections 3--4 of the upper-end theorem prove that the actual
complete first source can be paired with this last-rate
envelope on \(R\le7/10\). The inputs are its profile
inequalities (14)--(18), before multiplication by its
particular end sum: first main and real cuts have deficit
greater than \(10^{-10}\), and the first last alternative
has its explicit \(109/2000\) deficit. The original complete
cap and the full shared allocation stay attached.

Thus the first positive low block, complete middle integral
and all its weighted and unweighted currents, and positive
upper half/last alternatives may each be multiplied by (19).
Choosing the total finite tolerances inside those profile
reserves proves
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|\,
       \mathcal U_{0,N}^{\,78}(Y,Z)
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
\quad}                                                         \tag{20}
\]
The estimate holds for all real ordinary colors and arbitrary
subsets of (18). The forced \(d_N\) bound and the distinct
canonical factorial continuation through \(q=0\) are those
of the cited complete-first proof. No relative formula for
the forced weight is inserted.

## 5. A complete central next kernel on a smaller shared interval

If \(0\le q\le1/50\), then \(4/5-q\ge39/50\).
[The enlarged-band theorem](research_mixed_next_own_three_upper_band_old_face.md), combined there with the complete
signed below-half source, already pays every next index
\[
0\le j\le\lfloor N(4/5-q)\rfloor.
\]
Every remaining index lies in (18). Use its arbitrary-subset
version to partition the original sum without duplicating any
row. Thus (20) proves the complete finite estimate
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z)|
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}},
\quad
0\le q\le1/50,\quad R\le7/10 .
\quad}                                                         \tag{21}
\]
Here \(C_{0,N}\) is its literal full sum \(0\le j<N\).
Both index parities and all original carriers and zero rows
are included. There is no extra next-index density factor.

Integrating (20) or (21) over the central first incoming
interval retains the original \(+N\,da\), costing only a
polynomial. Fixed-base signed sums and these integrals have
normalized local mixed jets with gap \(10^{-12}\), by the
same all-real color and logarithmic-arc polynomial continuation
as the input theorems, followed by Cauchy's formula.
The actual reference and shared coordinate are fixed labels;
integer cuts are frozen for the partial-sum assertions.
No derivatives of a positive sum or moving cutoff are claimed.

For \(R\le7/10\), [the fixed-shared band](research_mixed_next_own_three_upper_band_fixed_shared.md) and (20)
leave only
\[
11/50<v<\min\{3/10,q+1/5\}
\tag{22}
\]
within the formerly unresolved strip \(q<v<q+1/5\).
For \(R>7/10\), neither (17) nor (20) is asserted.
Equation (21) concerns the central first incoming interval
only; it does not complete its other paths, the filtered
Fourier remainder, or an arbitrary short composition.
