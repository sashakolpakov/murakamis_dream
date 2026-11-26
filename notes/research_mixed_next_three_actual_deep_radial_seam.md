# Radial transport through the full lower periodic seam

Private research proof candidate, 8 November 2026. For the actual
composition words beginning \(343\), the complete source is
exponentially smaller than its geometric action on the whole positive
radial segment between the actual shared radius and one. The earlier
radial theorem reached only the last part of this segment. The new
argument transports the individual phase bounds from the actual
radius, before summing their contour contributions.

This also controls the old filtered kernel on the vertical periodic
seam. The two remaining upper middle intervals and the lower right
middle interval are not estimated here. No numerical evaluation or
modification of a frozen source is used.

## 1. The fixed geometric reference and the varying integration variable

Fix the original reference of a complete word in powers three and
four, beginning \(343\), with length \(m\ge5\). Use the conventions
of [the actual lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md):
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
 \quad h_t=\Im t_*,\quad h_z=\Im z_* .
\]
In particular
\[
 \frac7{10}<R_*=e^{2\pi h_y}<\frac{41}{50},\quad
 e^{2\pi h_s}>\frac45R_*,\quad
 -\frac3{100}<h_t,h_z<\frac1{50}.                         \tag{1}
\]
The original base reference is held fixed throughout the proof.
Only the integration variable varies:
\[
 y=ih,\quad h_y\le h\le0,\quad Y=e^{2\pi h},\qquad
 z=u+ih_z,\quad u\in P=[11/50,9/20].                     \tag{2}
\]
There is no claim that \(ih\) is another critical point.

Put \(D=N-1\), \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), and \(p_j(V)=(rV;r)_j\). The original
complete functions are
\[
\begin{split}
 C_{\beta,N}(V,W)
   &=\sum_{j=0}^{D}\frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},\\
 F_N(w,Y)
   &=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 \mathscr D_N(w,Y,Z)&=F_N(w,Y)d_N(Y)C_{0,N}(Y,Z),\qquad
 Z=e^{-2\pi iz}.
\end{split}                                                   \tag{3}
\]
Here \(U_{0,N}\) is the entire original cap, and \(d_N\) is
the forced polynomial with \(d_N(r^b)=P_b^{-1}\) and degree
at most \(D\). The first constant term retains its factor \(+N\).
There is no additional selected factor \(Y^{-N}\) in (3).

Write \(\Lambda_{123}(z)\) and \(\mathcal P_0^+(w,z)\) for the
unchanged affine bound and holomorphic critical action. At the
actual output,
\[
 \Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*).             \tag{4}
\]

**Theorem 1.** Uniformly on the actual references (1), for every
real ordinary color \(w\in[-2,2]\), both level parities, and
all sufficiently large \(N\),
\[
 |\mathscr D_N(w,R,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-10^{-13}\}},
 \qquad R_*\le R\le e^{-\pi/50},\quad z\in P+ih_z .       \tag{5}
\]
On fixed small neighborhoods of \(w=-2,z=z_*\), the same
source is exponentially smaller than \(e^{N\mathcal P_0^+}\)
throughout \(R_*\le R\le1\). A fixed complex tube about this
radial segment has the same conclusion with every fixed
normalized outside derivative and a smaller positive gap.

The last assertion uses the previously proved shallow-seam bound
near \(R=1\); it does not assert a canonical factorial expansion
at its singular endpoint.

## 2. Two monotonicity identities

The original primitive on the inward seam is
\[
 g(y)=\frac{\operatorname{Li}_2(e^{-2\pi iy})-\pi^2/6}{2\pi i},
 \qquad g'(y)=\operatorname{Log}(1-e^{-2\pi iy}).
\]
Consequently \(\Re g(ih)=0\) for \(h<0\), and continuously
at \(h=0\). Retain the literal phases
\[
 Q_\beta(v;b,c)=g(b+v)+g(c+v)-(2+\beta)g(v)
                  -g(b)-g(c)+2\pi ibv.                    \tag{6}
\]

For fixed \(s=v+i\sigma\), \(0<v\le1/2\),
\[
 \frac{\partial}{\partial h}\Re Q_1(s;a,ih)
   =-\operatorname{Arg}
       (1-e^{2\pi(h+\sigma)}e^{-2\pi iv})\le0.             \tag{7}
\]
The inequality is strict for \(0<v<1/2\); the argument is
zero at \(v=1/2\). The branch is the original one on
\(0<\Re(s+ih)<1\). For \(0<v<1/2\) the displayed complex
number is in the upper half-plane for every positive radius,
including when \(\sigma\) is an upper-alias height.

For a fixed next private index \(t=v+i\sigma\) in the same
real range,
\[
 \frac{\partial}{\partial h}\Re Q_0(t;ih,z)
   =-\operatorname{Arg}
       (1-e^{2\pi(h+\sigma)}e^{-2\pi iv})-2\pi v<0.        \tag{8}
\]
The final term is the original incoming carrier. Both identities
remain valid with any added Fourier phase depending on the private
index alone. They therefore apply separately to the main integral,
horizontal aliases, weighted vertical sides, and unweighted joins
when those paths are held fixed.

The next physical rows have a stronger finite statement:
\[
 R^{-j}|p_j(R)|=\prod_{\nu=1}^{j}|R^{-1}-r^\nu|
 \quad\hbox{is nonincreasing on }0<R\le1.                 \tag{9}
\]
Each factor decreases because
\(\partial_x|x-e^{i\theta}|^2=2(x-\cos\theta)\ge0\) for
\(x=R^{-1}\ge1\). Thus (9) holds before any limiting
rate is taken, including \(j=0\) and the true final index.
It bounds arbitrary positive subsets of next physical rows.

No monotonicity of a coherent finite sum is inferred from these
facts. The remaining proof applies them to the complete contour
decomposition and its explicit positive physical groups.

## 3. Transport of the complete following-kernel estimate

At \(Y=R_*\), the proof of
[the actual bounded-prefix theorem](research_mixed_next_three_actual_bounded_prefix.md)
bounds every retained next rate after adding
\[
                         B_0=2383/1500.                 \tag{10}
\]
The rates are the main at its original height \(h_t\), real
cuts \(3/20,1/2\), and all real upper rows. The proof gives a
margin strictly larger than \(1/200\) before its total finite
tolerance is spent. Its lower physical block and all canonical
currents are reduced to these rates before summation.

Freeze that decomposition at \(Y=R_*\). The lower private
currents have real coordinate between the low cut and the half
cut, up to the original \(O(N^{-1})\) grid displacement.
Their entire dependence on \(h\) at the exponential scale is
the dependence in (8). All extra cotangent/Fourier factors are
independent of \(h\). Positive next physical rows obey (9).
The exact forced-weight theorem,
[lower radial seam, Lemma 1](research_mixed_next_lower_radial_seam.md),
bounds the full \(d_N(R)\) by \(C_\tau N^B e^{N\tau}\) on
every fixed positive inward radial segment.

It follows, uniformly for \(R_*\le R\le e^{-\pi/50}\), that
\[
 |d_N(R)C_{0,N}(R,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-B_0-1/400\}}.            \tag{11}
\]
This is obtained from the profile proof, not from monotonicity of
the final signed kernel. Small half-grid displacements are
absorbed by the original uniform integrated-rate continuity.
For example a half cut displaced just beyond \(1/2\) has a
rate differing by \(o(1)\), uniformly on the present compact
radial interval. Its limit is covered by (8).

The original canonical identity is unchanged during this transport:
the denominator factorials of the private index have no new
\(h\)-dependent poles, and every shifted \(y+t\) retains its
real strip coordinate. The reciprocal factorial at \(y=ih\)
uses [the inward-seam continuation](research_factorial_symbol_across_inward_seam.md).
Here \(h\le-1/100\), so its compact-domain expansion remains
uniform. The old endpoint-uniform numerator bounds continue to
cover the half cut and physical zeros. There is no substitution
of that reciprocal factorial for \(d_N\).

## 4. The complete first integration

The six-piece incoming path is equation (6) of
[the actual lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md).
On its corner use the exact replacement rectangle of
[the actual right-path proof](research_mixed_next_three_actual_incoming_right_path.md).
The path, cuts, and private contours are now held at their
\(Y=R_*\) values while \(R\) increases.

The source proofs at \(R_*\) already bound each relevant
first phase together with each next phase. They retain
a profile deficit at least \(10^{-10}\), or the separate
bounded-factor margin. They are not consequences of taking
the modulus of the complete first integral. Their inventories
extend radially as follows.

| First incoming part | Dependence on the moving shared radius |
|---|---|
| Initial interval and taper | The main, real low and half profiles, and all canonical currents have private real coordinate in \([0,1/2]\). Their rates decrease by (7). The cap profiles are unchanged. |
| Central incoming interval | The main, both real cuts and every retained lower current obey (7). The first positive upper block has the original half/last envelope. |
| Right horizontal interval | Its complete low group has the whole-disk bound \(3111/2000<B_0\). All main and canonical-current profiles obey (7). |
| Replacement corner | Freeze the original first private deformation at its critical height for \(Y=R_*\). Each remaining main or side profile has real private coordinate in \([2/25,1/2]\), and obeys (7). The separate raw terms retain their whole-disk bound \(B_0+\tau\). |
| Far real interval | Its coherent complete cap-times-first estimate \(153/100<B_0\) holds on the entire disk \(|Y|\le1\). |

Here are the details concerning the first positive upper groups,
which are not covered directly by (7). For central incoming
\(x\in[11/50,9/20]\), the first-factor part of
[the upper-row theorem, Section 2](research_mixed_next_lower_left_own_four_upper_rows.md)
uses only \(0<R\le1\). It bounds the first upper rows by
\[
 \max\{E_1(1/2;a,ih),\delta_a\},\qquad
 \delta_a=-2\pi\Im a.                                    \tag{12}
\]
The half-row rate is constant in \(h\) by (7), and the last-row
rate is constant because the full numerator logarithmic mean is
zero for \(R\le1\). Thus the same two profiles as at \(R_*\)
remain valid.

For the initial interval and taper, Section 4 of
[the actual initial/taper proof](research_mixed_next_three_actual_incoming_initial_taper.md)
uses the half profile and the two alternatives
\(\delta_a,\delta_a+11/100\). Its first-source proof is
valid for every \(0<R\le1\). With the complete cap, the latter
groups have rates at most \(11099/7000\) and \(10813/7000\),
both below \(B_0\). The true cap endpoints have rate
\(389/300<B_0\). Its neighborhood of \(X=1\) has a uniform
whole-disk rate arbitrarily close to \(478/375<B_0\).
All these groups can therefore use (11) over the whole new
radial segment.

For the right horizontal segment the same first upper reduction
has half/last alternatives. Its complete cap-times-last rate is
\(11099/7000<B_0\), independent of \(R\). The other raw
group and the far interval are already listed in the table.

On the replacement corner, use the source-level decomposition
proved in Sections 5--6 of the actual right-path note. At
\(R_*\), its nonraw private profiles have rate at most the
critical value \(M(a,R_*)\); after multiplication by the cap,
each is bounded against every next profile there. The full
canonical main and connecting paths producing these inequalities
have private real coordinate in \([2/25,1/2]\). Both branches
of any incoming numerator wall have exactly the same dependence
\(g(ih+s)-g(ih)\) on the moving shared coordinate. Hence (7)
decreases their rates on these fixed paths. There is no need
to move the private critical point or claim a new Gaussian
asymptotic during this radial transport. The separated positive
rows and raw aliases have bounds on \(|Y|\le1\), and (11)
handles them with any prescribed extra tolerance.

The exact corner replacement remains valid for every \(R\),
since the original finite Laurent integrand is entire in the
incoming logarithmic variable. Both original sides are kept as
one oriented integral. No separate estimate for either original
corner side is deduced.

Apply (7)--(9) to the paired first and next profiles at \(R_*\),
and (11) to each of the raw groups just inventoried. Retain the
complete \(d_N\) and its arbitrarily small radial rate. The
canonical grids, their finite number of currents, the physical
sums, and the original first integration factor \(+N\) contribute
only polynomial prefactors. The fixed profile margins allow
their total finite tolerance to be chosen below half the
smallest margin. The conservative loss \(10^{-13}\) in (5)
follows. This proves the first part of Theorem 1.

## 5. The filter, the shallow endpoint, and complex neighborhoods

Keep the older \(11/12\) filter
\[
 F_N^{\rm mid}=F_N-E_N^{\rm filt},\qquad
 \sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
       \le CN^B e^{77N/50}.                              \tag{13}
\]
Since \(77/50<B_0\), (11) controls its complete correction
on the new radial segment. Therefore (5) also holds for
\[
          \mathscr D_N^{\rm mid}=F_N^{\rm mid}d_NC_{0,N}. \tag{14}
\]
This uses the actual old filter, not a replacement with a
different deleted band.

The old lower radial theorem already gives a fixed tube bound
on \([e^{-\pi/50},1]\) at every actual ordinary-three output,
with normalized gap \(1/1000\), including the same old filtered
source. Its hypotheses are imposed at the fixed actual reference.
Thus it overlaps the new segment at \(e^{-\pi/50}\) and supplies
the endpoint near one. The new segment is nonempty uniformly:
\(R_*<41/50<e^{-\pi/50}\), using
\(e^{-\pi/50}>1-\pi/50>164/175\).

We spell out why (5) also extends to a complex tube in \(Y\).
Both (3) and (14) have Laurent band \([-D,2D]\) in \(Y\)
and degree at most \(D\) in each outside polynomial variable
\(w,Z\). Cover the radial interval by short subintervals
\(I=[a,b]\), of uniformly positive chosen length, with
\(a\ge7/10\). The polynomial \(Y^D\mathscr D_N\) has degree
at most \(3D\). Its bound on \(I\) is the bound in (5) times
\(b^D\). The elementary Chebyshev ellipse inequality in
[polynomial continuation, Section 1](research_mixed_horizontal_complex_extension.md)
extends it to a small ellipse about \(I\), at cost
\(2(3D+1)\rho^{3D}\). Dividing by \(Y^D\) costs at most
\((b/\inf|Y|)^D\). First choose the subinterval length small,
and then choose \(\rho>1\) close to one. Both exponential
costs are arbitrarily small. Each ellipse contains its whole
interval, including its endpoints, in its interior.

A finite cover gives a fixed tube, uniformly for the compact
reference family. The same polynomial continuation for the
real color and output arc, (4), and continuity of the original
action give normalized value bounds on fixed outside
neighborhoods. Cauchy's formula on smaller neighborhoods
gives every fixed outside derivative. The resulting common
gap may conservatively be taken as \(10^{-15}\). The base
reference, incoming paths and radial endpoints are fixed
when differentiating.

This proves Theorem 1 and its filtered version. It does not
differentiate a moving critical point or a varying integer cut.

## 6. The entire periodic vertical segment

The paired kernel is
\[
 K_N(y)=\frac{N\mathscr D_N^{\rm mid}(w,Y,Z)}{1-Y^N},
 \qquad Y=e^{-2\pi iy}.                                  \tag{15}
\]
The deleted seam node gives \(F_N^{\rm mid}(w,1)=0\)
identically in the outside variables. Therefore
\(\mathscr D_N^{\rm mid}(w,1,Z)=0\).

On \(R_*\le Y\le1\), use the exact factorization
\[
 1-Y^N=(1-Y)\sum_{k=0}^{D}Y^k,\qquad
                          \sum_{k=0}^{D}Y^k\ge1.         \tag{16}
\]
The tube bound of Theorem 1 controls the divided difference
\(\mathscr D_N^{\rm mid}(Y)/(Y-1)\) near one by Cauchy's
formula. Away from one, division costs only a fixed constant.
Equations (15)--(16) thus control \(K_N\) on the entire lower
vertical segment, including its removable value at \(y=0\).
This step uses the zero of the complete filtered density;
an estimate of the denominator alone would not suffice there.

For \(1\le Y\le e^{\pi/50}\), retain the selected density
\(\mathscr D_{1,N}^{\rm mid}=Y^{-N}\mathscr D_N^{\rm mid}\).
The [upper radial theorem](research_mixed_next_upper_radial_seam.md)
bounds it on a fixed tube, with normalized gap \(1/1000\).
It also vanishes at \(Y=1\), and
\[
 K_N=-\frac{N\mathscr D_{1,N}^{\rm mid}}{1-Y^{-N}},
 \qquad
 \left|\frac{Y-1}{1-Y^{-N}}\right|
   =\frac{Y^N}{\sum_{k=0}^{D}Y^k}\le Y.                  \tag{17}
\]
The same divided-difference argument handles the upper
vertical segment. Periodicity identifies \(K_N(1+ih)\)
with \(K_N(ih)\).

Consequently the exact current of the right paired rectangle,
\[
                       V_N(1)=i\int_{h_y}^{1/100}
                                           K_N(1+ih)\,dh,
\]
satisfies, on smaller fixed outside neighborhoods,
\[
 \partial_w^j\partial_z^k
  [e^{-N\mathcal P_0^+(w,z)}V_N(1)]
                    =O_{j,k}(e^{-10^{-16}N}).             \tag{18}
\]
The path has uniformly bounded length and retains its original
orientation and the factor \(N\) already inside \(K_N\).
No other vertical current or half-grid term is removed.

A fixed small angular width also lies in the new tube at
\(Y=R_*\). Hence the lower endpoint arcs near both zero
and one have the same exponentially small normalized
contribution: on their actual lower height,
\(|Y^N|\le(41/50)^N\) bounds the denominator away from zero.
This extends the previously shallow lower-endpoint conclusion
to the entire actual family (1).

The middle of the lower-right interval and both upper middle
intervals still require comparison. In the right paired
rectangle identity, (18) controls its periodic seam current
\(V_N(1)\); the other vertical current and the even-level
half-grid term retain their separate obligations.

