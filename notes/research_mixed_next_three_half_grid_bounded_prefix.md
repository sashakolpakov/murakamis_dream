# A bounded preceding factor on the half-period side

Private research proof candidate, 8 November 2026. The complete next
type-three factor has a uniform attachment estimate on the selected
near-half interval and the original half-grid vertical. The allowable
preceding rate includes the original filter correction outside the
unit disk. Every physical index, contour current, and Fourier-weight
term is retained.

This does not assert that an arbitrary first incoming contribution
has the required bound. No mathematical numerical evaluation or
frozen-source modification is used.

## 1. Reference, finite functions, and statement

Use the original references of complete words in powers three and
four beginning \(343\), with length at least five. Keep the notation
and actual correlations of
[selected-left filter correction](research_mixed_next_three_selected_left_filter_correction.md).
In particular
\[
 \begin{gathered}
 c=\Im t_2^*,\quad h_t=\Im s_3^*,\quad h_z=\Im t_3^*,\quad
 H=1/100,\quad q_b=9/20,\\
 7/10<R_*=e^{2\pi c}<41/50,\qquad
 -3/100<h_t,h_z<1/50,\\
 z=u+ih_z,\quad 3/10\le u\le39/100,\quad Z=e^{-2\pi iz},\\
 B_0=2383/1500,\qquad B_f=77/50+\pi/50 .
 \end{gathered}                                                   \tag{1}
\]
The actual output is included in the stated real interval. The
affine comparison \(\Lambda_{123}(z)\) and the critical action
\(\mathcal P_0^+(w,z)\) retain their original constants and lifts.

For \(D=N-1\), \(r=e^{-2\pi i/N}\), put
\[
 P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,\quad
 C_{0,N}(Y,Z)=\sum_{j=0}^{D}
                 \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
 \tag{2}
\]
The degree-\(D\) bound and original values
\(d_N(r^b)=P_b^{-1}\) specify the complete forced polynomial.
Let
\[
 M_N=\lceil N/2\rceil,\qquad
 L_N=(M_N-\tfrac12)/N .
 \tag{3}
\]
These are the unchanged cut and half-grid of the right paired
rectangle.

**Theorem 1.** Let \(V_N\) be independent of the next private
index. On whichever of the following domains is used, assume
\[
                    |V_N|\le CN^a e^{NB_f}.
 \tag{4}
\]
For all sufficiently large \(N\) of both parities:

1. On \(y=q+iH,\ q_b\le q\le1/2\),
\[
 |V_Nd_N(Y)Y^{-N}C_{0,N}(Y,Z)|
       \le C' N^{a'} e^{N\{\Lambda_{123}(z)-1/1000\}}.
 \tag{5}
\]
2. On \(y=L_N+ih,\ c\le h\le H\),
\[
 \left|\frac{N V_Nd_N(Y)C_{0,N}(Y,Z)}{1-Y^N}\right|
       \le C' N^{a'} e^{N\{\Lambda_{123}(z)-1/1000\}}.
 \tag{6}
\]
Here \(Y=e^{-2\pi iy}\). The same pointwise allowance applies
to the lower horizontal segment \(q_b\le q\le1/2,\ y=q+ic\)
with its paired denominator.

No holomorphy of \(V_N\) is assumed in this theorem. In particular
it supplies no derivative conclusion for a preceding factor
specified only by (4).

## 2. The original negative-height calibration

Write
\[
 Q(t;y,z)=g(t+y)+g(t+z)-2g(t)-g(y)-g(z)+2\pi iyt,
 \quad G(y)=\Re g(y),
 \quad L(h)=2\pi(-h)_++2\pi(h_z)_+ .
 \tag{7}
\]
The main and real-cut profiles use respectively
\[
 t=v+ih_t,\quad 3/20\le v\le1/2,
 \qquad t=3/20,\ 1/2 .
 \tag{8}
\]
The last profile is \(L(h)\), not a value on a continued
central branch at index one.

The original lower-output low-block comparison, equations
(8)--(10) in
[its proof](research_mixed_conditional_lower_output_low_block.md),
is uniform on the whole unselected plateau \(q\in[.22,.45]\).
Together with the individual ordinary profile estimates in
[three-row assembly](research_mixed_three_row_source_assembly.md),
it gives at \(y_b=q_b+ic\)
\[
 \begin{split}
 B_0+\Re Q(t;y_b,z)-G(y_b)&<\Lambda_{123}(z)-1/50,\\
 B_0+L(c)-G(y_b)&<\Lambda_{123}(z)-1/50 .
 \end{split}                                                     \tag{9}
\]
The first line covers all profiles (8). The proof of that
calibration compares the constant preceding rate \(B_0\)
with the original allocated supporting plane, before finite
summation. It therefore supplies (9), rather than only an
estimate of the sum from which individual profile estimates
would not follow.

For clarity, the two marginal reserves in that proof are
\[
 \frac74-B_0-\frac{11}{80}=\frac{143}{6000}>\frac1{50},
 \qquad
 \frac74+\frac1{45}-B_0-\frac1{12}-\frac{801}{10000}
                 =\frac{1811}{90000}>\frac1{50}.
 \tag{10}
\]
They have no premise that \(q=.22\).

Keep height \(c\) and increase \(q\) from \(q_b\) to \(1/2\).
Put \(A=e^{-2\pi h_t}<11/9\) and
\(D_q=|1-R_*e^{-2\pi iq}|^2\). For a main profile,
\[
 e^{\partial_q(\Re Q-G)}
       =\frac{|A-R_*e^{-2\pi i(q+v)}|}{D_q}
       \le\frac{A+R_*}{D_q}<\frac{80}{117}<1 .
 \tag{11}
\]
At a real cut replace \(A\) by one. Indeed
\[
 D_q>\frac{39}{40}(1+R_*)^2,\qquad
 \frac{A+R_*}{(1+R_*)^2}
 \le\frac{11/9+7/10}{(1+7/10)^2}
       =\frac{1730}{2601}<\frac23 .
 \tag{12}
\]
These use \(\cos(2\pi q)<-19/20\); the last fraction
decreases with \(R_*\) after \(A\) is replaced by \(11/9\).
The last profile has derivative
\(\partial_q(L(c)-G)=-\log|1-Y|<0\).
Thus (9) holds throughout this lower interval. In particular,
since \(G(1/2+ic)=0\),
\[
 B_0+\phi(c)<\Lambda_{123}(z)-1/50
 \tag{13}
\]
for every main, cut, and last profile at its half-period endpoint.

## 3. Moving the endpoint to the selected height

First keep \(q=q_b\) and change the shared height from \(c\)
to \(H\). Let
\[
 \mathcal A(v,k)=\arg(1-e^{2\pi k-2\pi iv}),\quad
 \Phi(k)=\Re Q(t;q_b+ik,z),\quad G(k)=\Re g(q_b+ik).
 \tag{14}
\]
Every index in (8) has \(q_b+\Re t>1/2\). The elementary
argument bounds on the original strip give
\[
 \begin{array}{c|c|c}
 &c\le k\le0&0\le k\le H\\\hline
 (\Phi-G)'&\le0&\le\pi(1-2q_b)\\
 \Phi'&\le\pi(q_b-1/2)<0&\le0 .
 \end{array}                                                     \tag{15}
\]
For example
\(\Phi'=\mathcal A(q_b,k)-
\mathcal A(q_b+\Re t,k+\Im t)-2\pi\Re t\).
Below zero use
\(\mathcal A(q_b,k)\le\pi(1/2-q_b)\);
above zero use \(\mathcal A(q_b,k)\le\pi(1-2q_b)\).
The second argument has lower bound
\(\pi(1-2q_b-2\Re t)\) at every height. These give (15).

The selected factorial rate is \(\Phi(H)-G(H)-2\pi H\).
Its comparison with \(\Phi(c)-G(c)\) is nonincreasing
below height zero, and has derivative at most
\(-\pi(1+2q_b)<0\) above zero. The forcing rate is
\(\Phi(H)\); it is smaller still than the old unselected
rate because \(\Phi\) is nonincreasing and \(G(c)<0\).
The sign of \(G(c)\) is the original dilogarithm integral
on \(0<q_b<1/2,\ c<0\).

The last profile obeys the same conclusions. Below zero
\[
 \frac{d}{dk}\{L(k)-G(k)\}
   =-2\pi+\mathcal A(q_b,k)<0,
 \]
and above zero
\(\frac{d}{dk}\{L(k)-G(k)-2\pi k\}
=\mathcal A(q_b,k)-2\pi<0\).
For forcing, \(L(H)<L(c)-G(c)\).
Thus both selected alternatives at \(q_b+iH\) retain
the full reserve \(1/50\) in (9).

Now increase the selected real coordinate to \(1/2\).
The next-only comparisons in Section 2 of
[the near-half central theorem](research_mixed_next_three_selected_near_half_central.md)
apply independently of its first factor. A next main index
below \(11/50\) increases to that value. After this clipping,
put \(R=e^{2\pi H}\), \(D=|1-Y|^2\), and
\(U_2=|A-Re^{-2\pi i(q+v)}|^2\). That source proves
\[
 U_2/D<39/40<1,\qquad D>1 .
 \tag{16}
\]
It proves the same bound for both real cuts, with \(A=1\).
The derivatives of the next-only forcing and factorial rates
have exponential squares \(U_2/D\) and \(U_2/D^2\),
respectively. Both decrease. The last forcing profile is
constant, and its factorial weight decreases since \(D>1\).
We have therefore proved, on the whole top interval,
\[
 B_0+\phi(H)+W_\nu
              <\Lambda_{123}(z)-1/50,\qquad
 W_{\rm fac}=-G(y)-2\pi H,\quad W_{\rm force}=0 .
 \tag{17}
\]
At \(q=1/2\), the forcing choice gives the unweighted
upper endpoint \(B_0+\phi(H)<\Lambda_{123}(z)-1/50\).

## 4. The complete kernel between the two heights

At real coordinate \(1/2\), \(G(1/2+ih)=0\) for all \(h\).
For each fixed private index \(0<\Re t<1/2\),
\[
 \frac{d^2}{dh^2}\Re Q(t;1/2+ih,z)
         =-\pi\Re\cot\pi(1/2+ih+t)\ge0 .
 \tag{18}
\]
The incoming carrier is affine in \(h\). At the real half
index the same conclusion follows by the continuous limit;
the numerator wall has an upward derivative jump. The last
profile \(L(h)\) is convex as well. Equations (13),(17)
and this convexity imply
\[
 B_0+\phi(h)<\Lambda_{123}(z)-1/50
                             \quad(c\le h\le H)
 \tag{19}
\]
for every fixed next main, real-cut, or last profile.

The complete finite reduction to these profiles uses exactly
the next-kernel argument in Sections 4--5 of
[the central half-grid proof](research_mixed_next_three_central_half_grid_vertical.md).
Here are its source requirements, independent of any first factor.
The low real rows increase to \(3/20\), since their folded
incoming modulus is greater than \(15/16\), their outgoing
modulus exceeds \(7/5\), and their own squared denominator
is less than one. The zero row is included. The upper
physical rows reduce to the real half and last rates by
[transformed upper rows, Lemma 1](research_mixed_transformed_upper_rows.md).
Its entire angle square and height range contain these targets
at every intermediate height.

For the canonical middle sum retain cuts \(3/20,1/2\),
main height \(h_t\), and alias heights \(-1/5,8\).
Its index argument satisfies
\[
                -39\pi/50\le\Im Q_t\le11\pi/10
 \tag{20}
\]
throughout these heights. The proof uses only the sign of the
incoming shifted real coordinate \(q+\Re t>1/2\) and the
actual outgoing interval; it does not require a sign for
either shifted imaginary part. These inequalities bound
both horizontal aliases and the four weighted sides by
the same main and real-cut profiles. On both unweighted
joins the incoming cotangent is nonpositive, and the
original actual-height outgoing/own comparison gives
vertical convexity. The zero-safe period and reflection
bound covers the half-index numerator wall.

The literal cotangent identity keeps its \(+N\) main
measure, both aliases, four weighted sides and two joins.
The complete physical groups include their true integer
endpoints at both parities. All finite estimates have
polynomial costs and arbitrarily small rate tolerances.
Thus (17) bounds the full selected next factor on the
top interval; (19) bounds the full unweighted next kernel
at real coordinate \(1/2\).

At the original half-grid \(L_N\), the change from \(1/2\)
is at most \(1/(2N)\). The same uniform zero-safe estimates
and integrated-log continuity change the rate by
\(O((\log N)/N)\), including the numerator wall.
The full forced Fourier bound gives
\[
 |d_N(e^{-2\pi iy})|
 \le C_\tau N^b
 e^{N\{\max(-G(y),\,2\pi(\Im y)_+)+\tau\}}.
 \tag{21}
\]
On this vertical \(G(L_N+ih)=O(N^{-1})\), whereas exactly
\[
 Y^N=-e^{2\pi Nh},\qquad |1-Y^N|=1+e^{2\pi Nh}.
 \tag{22}
\]
Consequently
\[
             \frac{|d_N(Y)|}{|1-Y^N|}
                       \le C_\tau N^b e^{\tau N}.
 \tag{23}
\]
At height zero the denominator is two. No pole or Fourier
forcing term is removed by this estimate.

Finally
\[
 B_f-B_0<149/10500,\qquad
       1/50-149/10500=61/10500>1/200.
 \tag{24}
\]
Choose all finite tolerances inside this remaining reserve.
Equations (17),(19),(23) prove (5)--(6), with the more
conservative gap \(1/1000\). The lower horizontal claim
uses (11), the complete negative-height profile reduction,
and \(|1-Y^N|\ge1-R_*^N\). This proves Theorem 1.

## 5. The unchanged filter correction and its currents

Let \(E_N^{\rm filt}=F_N-F_N^{\rm mid}\) be exactly the
original correction in
[actual lower-half assembly, Section 4](research_mixed_next_three_actual_complete_lower_left.md).
Its degree in \(Y\) is at most \(D\), and
\[
 \sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
             \le CN^a e^{77N/50},\qquad -2\le w\le2 .
 \tag{25}
\]
For every \(|Y|\le e^{\pi/50}\), its reciprocal-polynomial
maximum principle gives
\[
 |E_N^{\rm filt}(w,Y)|
 \le CN^a e^{N\{77/50+\log_+|Y|\}}
 \le CN^a e^{NB_f}.
 \tag{26}
\]
It therefore satisfies (4) everywhere needed above.

Define
\[
 K_N^{\rm filt}(y)=
       \frac{N E_N^{\rm filt}(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},
 \quad
 V_N^{\rm filt}=i\int_c^H K_N^{\rm filt}(L_N+ih)\,dh .
 \tag{27}
\]
Let \(J_N^{\rm filt,grid}\) be its lower horizontal integral
from \(L_N+ic\) to \(1/2+ic\), minus its upper one from
\(L_N+iH\) to \(1/2+iH\). Equations (5)--(6) and the
lower horizontal statement bound both (27) and this grid
term below the geometric exponential rate. The fixed heights
keep the two horizontal denominators bounded away from zero.
No bound is inferred merely from their short lengths.

The numerator is polynomial of degree at most \(D\) in each
outside variable \(w,Z\). Polynomial continuation from their
real color interval and outgoing arc, followed by Cauchy's
formula and the unchanged normalization
\(\Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*)\), gives
\[
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_0^+(w,z)}
       \{V_N^{\rm filt}-J_N^{\rm filt,grid}\}\right]
                 =O_{j,k}(e^{-N/10000})
 \tag{28}
\]
on smaller fixed outside neighborhoods. The same conclusion
holds for either term separately and for the top correction
integral on any subinterval of \([9/20,1/2]+iH\).
Paths, heights and integer cutoffs stay fixed when these
outside derivatives are taken.

This pays the actual old filter contribution to the half-grid
side and its grid correction. The preceding factor in (4)
may also be an already bounded complete incoming contribution,
but the theorem does not supply (4) for the remaining incoming
paths. The coherent middle insertion and the unproved
noncentral first contributions remain in the exact source.
