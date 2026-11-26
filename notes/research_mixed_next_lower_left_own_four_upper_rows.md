# Upper own-four physical rows on the lower left interval

Private research deduction, 8 November 2026. On the lower left
domain, every upper physical row of the first own-four conditional
factor is bounded by its half-row or its last-row rate. The same
is true of the next conditional factor when its own type is four.
The proof keeps the complete positive physical blocks and their
original incoming carriers. It does not pay the last-row alternatives
or establish the analogous next own-three statement.

No numerical evaluation or modification of a frozen source is used.

## 1. Exact rates and reflection

Use the actual ordinary-next domain of
[the low physical-block theorem](research_mixed_next_lower_left_low_physical_blocks.md):
\[
\begin{gathered}
a=x+ih_a,\quad x\in P=[.22,.45],\quad -.072<h_a<0,\\
y=q+ih_y,\quad q\in[0,.22],\quad -.102<h_y<-.001,\\
z=u+ih_z,\quad u\in P.
\end{gathered}
\tag{1}
\]
In the second assertion below the next own type is four, so
\(h_z<0\). Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\),
\(Z=e^{-2\pi iz}\), \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), \(p_j(W)=(rW;r)_j\).

For any two negative-height arguments \(b,c\), retain the
original own-four row rate
\[
E_1(t;b,c)=
\int_0^t\log|1-e^{-2\pi i(b+s)}|\,ds+
\int_0^t\log|1-e^{-2\pi i(c+s)}|\,ds
-3J(t)-2\pi t\Im b .
\tag{2}
\]
Write \(T_b=e^{-2\pi\Im b}>1\), \(R_c=e^{2\pi\Im c}<1\),
and set \(\Phi(v)=E_1(1-v;b,c)-E_1(1;b,c)\).
Combining the first carrier with its incoming numerator
gives the exact reflected formula
\[
\Phi(v)=3J(v)
-\int_0^v\log|T_b-e^{-2\pi i(\Re b-s)}|\,ds
-\int_0^v\log|1-R_ce^{-2\pi i(\Re c-s)}|\,ds .
\tag{3}
\]
There is no independent drift to discard. In particular
\(E_1(1;b,c)=-2\pi\Im b\).
The original outer halfweight allocations are independent
of \(t\), so all comparisons below retain them unchanged.

We use the radial log-arc facts from
[right-tail reflection, Sections 1--2](research_mixed_right_tail_reflection.md).
For \(0<R\le1\), let
\[
G_R(t)=\int_0^t\log|1-Re^{-2\pi is}|\,ds .
\]
Then \(G_R(t)\ge J(t)\) on \(0\le t\le1/2\).
The radial log modulus is even and increases with distance
from the nearest integer. Every arc of length \(v\le1/2\)
therefore has integral at least \(2G_R(v/2)\).
An arc \([b-v,b]\subset[0,1/2]\), with \(b\ge v\),
has integral at least \(G_R(v)\).
For a folded radius \(T\ge1\), its modulus is pointwise at
least the unit-radius chord; hence its centered-arc lower
bound is at least \(2J(v/2)\).
All these statements include integrable zero-height limits.

Finally, concavity of \(\log(2\sin\pi t)\) gives
\[
2\{J(v)-J(v/2)\}
 \le v\log\{2\sin(3\pi v/4)\}<0,
\qquad 0<v<2/9.
\tag{4}
\]

## 2. The first conditional factor

Take \((b,c)=(a,y)\). If \(0\le v\le1/5\),
the first arc in (3) lies in \([0,1/2]\), since
\(x\ge.22>v\). Its integral is at least \(J(v)\).
The second arc has integral at least \(2J(v/2)\).
Thus (3)--(4) imply \(\Phi(v)\le0\): these rows are
bounded by their literal last-row rate.

For \(1/5\le v\le1/2\), subtract \(\Phi(1/2)\) in (3).
For every integration coordinate \(s\in[v,1/2]\),
\(|x-s|\le7/25\), and \(T_a<8/5\). Since
\(\cos(14\pi/25)>-1/5\),
\[
|T_a-e^{-2\pi i(x-s)}|^2
<\frac{64}{25}+1+\frac{16}{25}=\frac{21}{5}.
\]
The logarithm of this modulus is less than \(3/4\):
\(e^{3/2}>1+3/2+(3/2)^2/2+(3/2)^3/6+(3/2)^4/24>21/5\).
The second modulus is at most two, whose logarithm is
less than \(7/10\). Consequently
\[
\Phi(v)-\Phi(1/2)
\le\frac{29}{20}(1/2-v)+3J(v).
\tag{5}
\]
The right side is convex on \([1/5,1/2]\).
It is zero at \(1/2\), and strictly negative at \(1/5\).
For an explicit witness, the elementary Catalan estimate
in [the half-interval packet, equation (21)](research_repeated_two_block_half_interval_packet.md)
gives
\[
-J(1/4)>\frac{63}{440}>\frac7{50}.
\]
Also \(2\sin(\pi/5)>7/6\) and
\(\log(7/6)>2/13\), so
\[
-J(1/5)>
\frac7{50}+\frac1{20}\log(7/6)>
\frac{48}{325}.
\tag{6}
\]
The chord witness follows from
\(\sqrt5<41/18\), and the logarithm witness is its first
positive \(\operatorname{arctanh}\) term.
At \(v=1/5\), (5) is therefore less than
\[
\frac{87}{200}-\frac{144}{325}=-\frac{21}{2600}<0.
\tag{7}
\]
Convexity proves that all remaining rows are bounded by
their half-row rate. Together with the small-\(v\) case,
\[
\boxed{\quad
\max_{1/2\le t\le1}E_1(t;a,y)
=\max\{E_1(1/2;a,y),E_1(1;a,y)\}.
\quad}
\tag{8}
\]

## 3. The next own-four factor

Now take \((b,c)=(y,z)\), with \(h_z<0\).
For \(0\le v\le11/50\), the outgoing arc lies in
\([0,1/2]\), because \(u\ge11/50\ge v\).
Its integral is at least \(G_{R_z}(v)\ge J(v)\);
the incoming folded arc is at least \(2J(v/2)\).
Equation (4) again gives \(\Phi(v)\le0\).

For \(11/50\le v\le1/2\), the incoming folded modulus
is less than three, because \(T_y<2\), and its logarithm
is less than \(11/10\). On the outgoing arc
\(|u-s|\le7/25\), and \(R_z\le1\). Convexity of its
squared modulus in \(R_z\in[0,1]\) gives
\[
|1-R_ze^{-2\pi i(u-s)}|^2
\le\max\{1,2-2\cos(14\pi/25)\}<\frac{12}{5}
<\left(\frac85\right)^2.
\]
Its logarithm is less than \(1/2\), since
\(e^{1/2}>1+1/2+(1/2)^2/2=13/8>8/5\).
Thus
\[
\Phi(v)-\Phi(1/2)
\le\frac85(1/2-v)+3J(v).
\tag{9}
\]
This is convex on \([11/50,1/2]\), with value zero
at its right endpoint. At the left endpoint,
\(2\sin(11\pi/50)>5/4\), as proved in the low-block note,
and \(\log(5/4)>2/9\). Therefore
\[
-J(11/50)>
\frac{63}{440}+\frac3{100}\log(5/4)>
\frac{989}{6600}.
\tag{10}
\]
The value in (9) is less than
\[
\frac{56}{125}-\frac{989}{2200}
=-\frac{17}{11000}<0.
\tag{11}
\]
This proves
\[
\boxed{\quad
\max_{1/2\le t\le1}E_1(t;y,z)
=\max\{E_1(1/2;y,z),E_1(1;y,z)\}.
\quad}
\tag{12}
\]
All scalar witnesses are written inequalities; no action
value or reference point is evaluated.

## 4. Complete finite positive blocks and scope

The uniform original sine-factorial estimate through both
end indices and the zero-safe numerator bounds convert
(8),(12) into the positive finite inequalities
\[
\begin{split}
\sum_{\lceil N/2\rceil\le j<N}
\left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
&\le C_\tau N^{B_\tau}
 e^{N\{\max(E_1(1/2;a,y),E_1(1;a,y))+\tau\}},\\
\sum_{\lceil N/2\rceil\le j<N}
\left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^3}\right|
&\le C_\tau N^{B_\tau}
 e^{N\{\max(E_1(1/2;y,z),E_1(1;y,z))+\tau\}}.
\end{split}
\tag{13}
\]
The second line is only for next own type four.
Both parities, every indicated physical row and all numerator
zeros are retained. The continuum endpoint \(t=1\) bounds
the actual last index \(j=N-1\) with the original uniform
\(O(\log N)\) error; no new row \(j=N\) is inserted.
If a half-grid decomposition shifts its first upper row
by \(O(1)\) indices, continuity at the half cut and the
same tolerance give (13).

All outside row-independent allocations remain attached.
Subsets inherit the positive bound. Fixed ordinary-color
derivatives act on a separately attached complete cap;
fixed outside derivatives follow on smaller neighborhoods
from the strict compact source inequalities, with polynomial
costs and a prescribed tolerance. The partial row sums
themselves have no extra coefficient-extraction factor \(N\).

The half-row alternatives in (13), paired with an eligible
main or real-cut profile of the other conditional factor,
have the comparison already proved in the joint profile
theorem. The last-row alternatives are still literal.
In particular (13) is not an upper bound for either whole
factor below the next action plane, and it does not pay
last-by-main, last-by-last or the remaining next own-three
upper block. No whole next-transfer conclusion follows.
