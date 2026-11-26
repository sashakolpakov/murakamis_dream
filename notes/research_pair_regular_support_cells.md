# Exact wire cells for the regular physical support

Research calculation, 4 November 2026. Frozen manuscripts are unchanged.

The normal-defect formula permits the low internal pair to be
interpolated without the original off-grid first normals. This
interpolation is an entire finite Fourier function and agrees with
every retained original coefficient. Within one wire cell its
physical rows can be restricted to the regular value support.
When the cells are joined, their shared faces contribute explicit
currents. Those currents are retained below; the regular support
alone does not prove that they have a smaller exponential rate.

The statement concerns even levels. The odd trace has an additional
top-degree contribution and is not silently identified with this
formula.

## 1. The original physical-row interpolant

Let \(N=2m\), \(\theta=\pi/N\), and use
\[
 c_a=2\cos((2a+1)\theta),\quad 0\le a<m,\qquad
 Q(z)=2T_m(z/2),\qquad
 S_j=\prod_{r=1}^j2\sin(r\theta).
 \tag{1}
\]
For each distinct physical row define
\[
 \begin{split}
 B_a(x)
 &=\frac{\sin(\pi Nx)}{N\sin(\pi x)}
       \prod_{r=1}^{a}
          \frac{\sin\pi(x+r/N)}{\sin\pi(r/N-x)}\\
 &=\frac{2^{N-1}}N
       \prod_{r=1}^{N-a-1}\sin\pi(x+r/N)
       \prod_{r=1}^{a}\sin\pi(x+r/N).
 \end{split}
 \tag{2}
\]
All apparent poles in the first line are removable.

**Lemma 1.** The function \(B_a\) is entire, with frequencies
\(-(N-1)/2,\ldots,(N-1)/2\), and
\[
 B_a(j/N)=
 \begin{cases}
 e_j(c_a)=S_{a+j}/(S_{a-j}S_j^2),&0\le j\le a,\\
 0,&a<j<N.
 \end{cases}
 \tag{3}
\]
It is the original finite Fourier interpolant of this row.

*Proof.* The finite sine product
\(\sin(Nv)=2^{N-1}\prod_{r=0}^{N-1}\sin(v+r\pi/N)\)
gives the second line of (2), after canceling the factors
with \(r=N-a,\ldots,N-1\).
There are exactly \(N-1\) sine factors, proving the frequency
statement and \(B_a(x+1)=-B_a(x)\).
At \(j>a\), the factor with \(r=N-j\) is zero.
At \(0\le j\le a\), cancel the simple zero in the first
line of (2); the remaining sine products give (3).
These are the direct physical Newton values.
An \(N\)-dimensional consecutive Fourier band is determined
by its values at these \(N\) grid points, proving the last
assertion. \(\square\)

The same formula follows directly from the
[canonical factorial](exact_factorial_interpolation_and_complex_contours.md):
at the physical angle \(\tau_a=\pi-(2a+1)\pi/N\),
\[
 B_N(x,\tau_a)=\frac{G_N(a+Nx)}
                         {G_N(a-Nx)G_N(Nx)^2}.
\]
The shift relation and
\(G_N(z)G_N(-z)=N\sin(\pi z/N)/\sin(\pi z)\)
reduce this expression to (2). Thus the identity with
the factorial representative holds for complex \(x\),
not only at the interpolation nodes.

Let \(\ell_a(z)\) be the ordinary cardinal polynomial for
the nodes in (1), and put
\[
                    P_x(z)=\sum_{a=0}^{m-1}B_a(x)\ell_a(z).
 \tag{4}
\]
This polynomial has degree less than \(m\).
At every low grid index it is exactly \(e_j(z)\);
at every high grid index \(m\le j<N\) it is zero.
Its off-grid first normals are those of this ordinary
interpolant. They are not asserted to equal the first
normals of the full original Fourier representative.
Equality at the retained discrete indices is what is
needed for the finite sum.

## 2. An entire interpolation of the complete low source

Use the complete low polynomial \(\mathcal L_N\) and the
holomorphic defect \(\mathscr D_{n,N}\) from
[the observation theorem](research_complete_source_pick_observation.md#7-complex-colors-and-the-exact-normal-defect).
Thus, after removing the scalar crossing carrier,
\[
 h_{n,N}(z)=
   e^{inN\arccos(-z/2)^2/(4\pi)}\mathcal L_N(z),\qquad
 \mathscr D_{n,N}=(h_{n,N}-\mathcal I_{n,N})/Q.
 \tag{5}
\]
Here \(\mathcal I_{n,N}\) is the ordinary value interpolant
of \(h_{n,N}\), and the difference in (5) removes all its
physical zeros before division. Define
\[
 u_{n,a}=\eta C_{N,n}N^2
                  \frac{\mathscr D_{n,N}(c_a)}{Q'(c_a)},
 \qquad
 \widetilde W_{n,N}(x)=\sum_{a=0}^{m-1}u_{n,a}B_a(x),
 \tag{6}
\]
where \(\eta=(-1)^{N-1}\) and
\(C_{N,n}=\exp(\pi i n(N-1)^2/(4N))\).

**Theorem 2.** At every level,
\[
 \begin{split}
 \widetilde W_{n,N}(x)
       &=\phi_N[R^n\mathcal L_N P_x],\\
 \widetilde W_{n,N}(j/N)
       &=\phi_N[R^n\mathcal L_Ne_j]\quad(0\le j<m),\\
 \widetilde W_{n,N}(j/N)&=0\quad(m\le j<N).
 \end{split}
 \tag{7}
\]
Consequently the pair with all three indices restricted
to the literal low range has the exact representation
\[
 \begin{split}
 \mathcal P^{\mathrm{all\,low}}_{n,p,N}
  &=\sum_{j=0}^{m-1}
       \widetilde W_{n,N}(j/N)\widetilde W_{p,N}(j/N)\\
  &=N\int_{iY}^{1+iY}
       \widetilde W_{n,N}(x)\widetilde W_{p,N}(x)\,dx
                           \qquad(Y\in\mathbb R).
 \end{split}
 \tag{8}
\]

*Proof.* The original normal-defect trace identity applies
to \(P_x\), whose degree is less than \(m\). At the even
physical roots,
\((4-c_a^2)Q'(c_a)^2=N^2\).
This gives the first line of (7) with every original normal
retained in \(\mathscr D_{n,N}\).
Lemma 1 gives the other two lines.
The product in (8) has integral frequencies in
\([-(N-1),N-1]\). Its \(N\)-point discrete average and
its period integral both select precisely the constant
coefficient. Vertical translation does not change that
coefficient. This proves (8), without any asymptotic
or replacement of the original discrete source. \(\square\)

For fixed positive integer \(n,p\ge3\), the
[original radical-sector estimate](research_internal_pair_combined_contour_reduction.md#2-uniform-removal-of-the-original-real-tails)
bounds the difference between this low pair and the full
three-edge source by a polynomial times \(e^{2NM_\infty}\).
The pair's geometric rate exceeds \(2M_\infty+1/100\).
Thus (8) retains the part whose global coefficient is
still required; it does not use a kernel approximation
to discard an uncontrolled radical.

## 3. Removing the below-support rows within one cell

For \(0\le j<m\), put
\[
 A_{n,j}(x)=\sum_{a=j}^{m-1}u_{n,a}B_a(x),\qquad
 F_j(x)=A_{n,j}(x)A_{p,j}(x).
 \tag{9}
\]
Fix \(Y>0\), let \(\Omega_j\) be the counterclockwise
rectangle with real sides \((j\pm1/2)/N\) and imaginary
heights \(\pm Y\), and set
\[
                         k_N(x)=\pi N\cot(\pi Nx).
 \tag{10}
\]
This kernel has residue one at \(j/N\).

**Proposition 3.** The exact low pair is
\[
 \mathcal P^{\mathrm{all\,low}}_{n,p,N}
          =\frac1{2\pi i}
                \sum_{j=0}^{m-1}
                     \oint_{\partial\Omega_j}k_N(x)F_j(x)\,dx.
 \tag{11}
\]
In each cell all rows \(a<j\) have been removed exactly,
not estimated.

*Proof.* At \(x=j/N\), Lemma 1 gives
\(A_{n,j}(j/N)=\widetilde W_{n,N}(j/N)\).
Every \(A_{n,j}\) is entire, and the cell contains only
one pole of \(k_N\). The residue theorem gives (11).
More explicitly, for \(a<j\), (2) has the form
\[
 B_a(x)=\sin(\pi Nx)\,G_a(x),\qquad
 G_a(x)=\frac1{N\sin(\pi x)}
             \prod_{r=1}^a
               \frac{\sin\pi(x+r/N)}{\sin\pi(r/N-x)},
 \tag{12}
\]
where \(G_a\) is holomorphic throughout \(\Omega_j\).
Its possible real poles lie at \(0,1/N,\ldots,a/N\)
modulo integers, outside this cell.
Multiplication by \(k_N\) removes the sine factor through
\(k_N(x)\sin(\pi Nx)=\pi N\cos(\pi Nx)\).
Thus the difference between the full and retained products
has zero contour integral cell by cell. \(\square\)

Each \(A_{n,j}\) can itself be written as
\[
 A_{n,j}(x)
   =\frac{\eta C_{N,n}N^2}{2\pi i}
        \oint_{\Gamma_j}
          \frac{\mathscr D_{n,N}(z)P_x(z)}{Q(z)}\,dz,
 \tag{13}
\]
where \(\Gamma_j\) encloses only the roots \(c_a\) with
\(a\ge j\). The ordinary interpolant \(P_x\) can be
replaced on this contour by the original factorial
interpolant \(B_N(x,t)\), \(z=-2\cos t\), whenever it
is holomorphic on the contour and its interior: only
the physical values enter the simple residues in (13).
No matching of its off-grid first normals is required.

The positive physical angles retained in (13) satisfy
\[
 0<\tau_a\le\pi-(2j+1)\pi/N,\qquad
                      j/N+\tau_a/(2\pi)<1/2.
 \tag{14}
\]
For \(j\ge1\), an angular cut at
\(T_j=\pi-2\pi j/N\) lies between the retained and omitted
physical rows. On the wire cell one has
\[
 \frac12-\Re x-\frac{|\Re t|}{2\pi}\ge-\frac1{2N}
                  \qquad(|\Re t|\le T_j).
 \tag{15}
\]
Thus this construction reaches at most an \(O(N^{-1})\)
neighborhood of the regular factorial boundary; it does
not introduce the previous reflected region of fixed
positive width. The first cell can use a cut strictly
between \(\pi-\pi/N\) and \(\pi\).
Equation (15) is a statement about contour locations,
not an asymptotic estimate at a factorial endpoint.
Such endpoint estimates and all vertical connectors
must still be proved or supplied by the existing
uniform factorial bounds.

## 4. The exact currents when the cells are joined

Set \(q_j=(j+1/2)/N\) for \(-1\le j<m\). Joining the
rectangles in (11) leaves their two horizontal sides,
the two outer vertical sides, and the following shared
vertical currents:
\[
 \frac1{2\pi i}\sum_{j=0}^{m-2}
     \int_{q_j-iY}^{q_j+iY}
                     k_N(x)\{F_j(x)-F_{j+1}(x)\}\,dx.
 \tag{16}
\]
The orientation is upward. The horizontal contributions
are, explicitly,
\[
 \frac1{2\pi i}\sum_{j=0}^{m-1}
 \left\{\int_{q_{j-1}-iY}^{q_j-iY}k_NF_j\,dx
             -\int_{q_{j-1}+iY}^{q_j+iY}k_NF_j\,dx\right\},
 \tag{17}
\]
with the right outer side using \(F_{m-1}\) upward
and the left outer side using \(F_0\) downward.

The shared-face integrand is completely explicit:
\[
 \boxed{\quad
 F_j-F_{j+1}
   =u_{n,j}B_j A_{p,j+1}
       +u_{p,j}B_j A_{n,j+1}
       +u_{n,j}u_{p,j}B_j^2 .
 \quad}
 \tag{18}
\]
Indeed \(A_{n,j}=A_{n,j+1}+u_{n,j}B_j\), and similarly
for \(p\). In particular a shared face inserts the
actual row \(j\) at one or both vertices. These are
ordinary value-support residues, with their normal
data already in \(u_{n,j}\). They are not deleted-edge
terms and need not vanish.

Equations (11), (16)–(18) describe the full finite
cycle after restricting each cell to its regular
physical support. They explain both the benefit and
the remaining cost of this change of representation.
There is no missing moving-pole term: it is precisely
the row insertion in (18). A global deformation must
bound or combine these currents along with the
horizontal and outer pieces. Local nonvanishing of
\(\mathscr D_{n,N}\) at a geometric pair angle, by itself,
does not settle that comparison.

## 5. A termwise absolute bound fails for the actual short pair

The three terms in (18) cannot in general be bounded separately
by the filled-pair rate. This can be proved for the actual source,
without choosing an artificial input vector.

Let \(n=p=3\), take \(N\) through multiples of six, and put
\(j=N/3\). On the shared face choose the short vertical segment
\[
 x_y=\frac{j+1/2+iy}{N},\qquad 1/10\le y\le1/5.
 \tag{19}
\]
Write \(\mu_3\) for the real half-charge action in the
[observation theorem](research_complete_source_pick_observation.md#5-a-nonzero-half-charge-observation),
and set
\[
 c=J(2/3)-2J(1/3)=-3J(1/3)=2J(5/6).
 \tag{20}
\]
The last identity follows from the sine duplication formula
and \(J(1-x)=-J(x)\).

**Proposition 4.** The third row-insertion term in (18) has
\[
 \lim_{\substack{N\to\infty\\6\,\mid\,N}}
 \frac1N\log
 \int_{1/10}^{1/5}
   \left|k_N(x_y)\,u_{3,j}^{\,2}B_j(x_y)^2\right|
                                 \frac{dy}{N}
                     =2\mu_3+2c>\frac{137}{50}.
 \tag{21}
\]
In contrast, the proved complete-boundary rate of the full
signed \((3,3)\) pair is less than \(13/5\).
Thus an upper bound for the absolute integral of this term
at the filled-pair rate is false. No assertion about the
rate of the *grouped* current (18) follows from (21).

*Proof.* The
[uniform physical-row defect theorem](research_physical_normal_defect_packet.md)
gives a nonzero rational leading coefficient for
\(\mathscr D_{3,N}(c_j)\). Since \(c_j\to-1\) and
\[
 \frac1{|Q'(c_j)|}
              =\frac{2\sin((2j+1)\pi/N)}N,
\]
there are fixed positive constants with
\[
       c_1N^{-1}e^{N\mu_3}
            \le |u_{3,j}|\le C_1N^{-1}e^{N\mu_3}.
 \tag{22}
\]
The original factorial estimate at the fixed arguments
\(1/3,2/3\) gives
\[
 B_j(j/N)=e_j(c_j)=S_{2j}/S_j^2
                         =\exp\{Nc+O(\log N)\}.
 \tag{23}
\]

The displacement in (19) changes the logarithm of this
finite product by only \(O(\log N)\), uniformly in \(y\).
Here is an explicit reason that also gives a lower bound.
In the second line of (2), evaluated at \(x=j/N\),
the sine arguments have integer numerators
\(k=j+1,\ldots,N-1\), and a second copy with
\(k=j+1,\ldots,2j\).
Under (19) each numerator becomes \(k+1/2+iy\).
Put \(q=N-k\ge1\). Along the straight displacement,
the real distance of the argument from the zero at \(1\)
is at least \(q/(2N)\); its distance from the other zero
is bounded below because \(k\ge N/3\).
The identity \((\log\sin z)'=\cot z\) and
\(|\sin z|\ge|\sin\Re z|\) therefore give
\[
 \left|
 \log\frac{\sin(\pi(k+1/2+iy)/N)}{\sin(\pi k/N)}
 \right|\le\frac{C}{N-k},
 \tag{24}
\]
with the logarithm continued along this zero-free segment.
One may obtain this bound directly from
\(\sin r\ge2r/\pi\) for \(0\le r\le\pi/2\)
and boundedness of \(\cos z\) on the indicated thin strip.
Summing (24) over both copies gives \(O(\log N)\).
Consequently
\[
                    |B_j(x_y)|=\exp\{Nc+O(\log N)\}
 \tag{25}
\]
uniformly on the entire interval of \(y\), with both
upper and lower bounds.

Finally
\[
             |k_N(x_y)|=\pi N\tanh(\pi y),
\]
which is bounded above and below by positive multiples
of \(N\). Equations (22) and (25), together with the
length element \(dy/N\), prove the limit in (21).

For the strict rational comparison, the half-charge
action estimate gives
\[
 \mu_3>M_\infty-\frac{\log3}{12}>
       \frac{23}{20}-\frac1{10}=\frac{21}{20}.
 \tag{26}
\]
Here
\[
 M_\infty>
 \frac{4(1-1/9+1/25-1/49)}{22/7}>\frac{23}{20},
 \qquad \log3<6/5.
 \]
The three-term positive Fourier-series bound in
[the complete-cap calculation](research_positive_three_crossing_cap_seed.md#2-sharp-third-moment-and-longer-actual-capped-chains)
gives \(c>8/25\). Thus \(2\mu_3+2c>137/50\).
The [validated original saddle record](../repro/results/research-internal-pair-three-mixed-packet.json)
encloses its one-vertex mixed action below \(13/10\);
the [full pair theorem](research_internal_pair_three_full_boundary_packet.md)
identifies twice that real action as the pair rate.
Hence the full rate is less than \(13/5<137/50\).
This proves the proposition. \(\square\)

This obstruction concerns an absolute estimate of one
specified term of an exact shared face. It does not
exclude cancellation within its complex integral,
between the three terms in (18), or with the adjacent
horizontal pieces. Those are precisely the comparisons
that a further global proof must preserve.

## 6. Exact grouping into finitely many support blocks

The moving-support jumps can be canceled before taking absolute
values. The exact price is that a block uses the support of its
leftmost cell, rather than the narrower support at each later
index. This reformulation does not assert a new exponential gap.

**Proposition 5.** Let \(0\le L\le R<m\), and let
\(\Omega_{L,R}\) be the counterclockwise rectangle with real
sides \(q_{L-1}\), \(q_R\) and imaginary heights \(\pm Y\).
Then
\[
 \sum_{j=L}^{R}
   \widetilde W_{n,N}(j/N)\widetilde W_{p,N}(j/N)
   =\frac1{2\pi i}\oint_{\partial\Omega_{L,R}}
                     k_N(x)F_L(x)\,dx.
 \tag{27}
\]
All original source data and normals remain those in (6).

*Proof by residues.* At each \(j/N\) in this block, every row
\(a<L\) vanishes by (3). Thus
\(A_{n,L}(j/N)=\widetilde W_{n,N}(j/N)\), and similarly for
\(p\). The integrand in (27) has only the simple wire poles
\(j/N\), \(L\le j\le R\), each of residue \(F_L(j/N)\).
This proves (27) directly.

The same cancellation can be seen in the joined currents.
Put \(G_j=k_N(F_j-F_{j+1})\). By (18), \(F_j-F_{j+1}\)
contains a factor \(B_j\), which vanishes at every later
wire node \(k/N\), \(k>j\). Consequently all apparent wire
poles of \(G_j\) in the slab \(q_j\le\Re x\le q_R\) are
removable. No residue is lost when its vertical face is
moved to the common right side \(q_R\). Explicitly,
\[
 \begin{split}
 \int_{q_j-iY}^{q_j+iY}G_j\,dx
 ={}&\int_{q_R-iY}^{q_R+iY}G_j\,dx\\
 &+\int_{q_j-iY}^{q_R-iY}G_j\,dx
       -\int_{q_j+iY}^{q_R+iY}G_j\,dx .
 \end{split}
 \tag{28}
\]
On the common vertical line,
\(\sum_{j=L}^{R-1}(F_j-F_{j+1})=F_L-F_R\).
On the horizontal segment of cell \(k\), the added connectors
sum to \(F_L-F_k\). Combining these with the original right
side and horizontal pieces in (16)–(17) leaves exactly the
single block boundary in (27). This also proves the formula
with all moving-face currents explicitly accounted for.
\(\square\)

Fix \(0<\varepsilon<1/2\). A retained consecutive set of low
indices can be partitioned into at most
\(\lceil1/(2\varepsilon)\rceil\) blocks with
\(R-L\le\lfloor\varepsilon N\rfloor\), by taking blocks of
at most \(\lfloor\varepsilon N\rfloor+1\) indices.
Only this fixed number of block contours is then needed,
independently of \(N\). At their common sides the grouped
jump is \(k_N(F_{L_{\rm left}}-F_{L_{\rm right}})\);
it has not been estimated or discarded.

The support restored within a block is precise. At a later
index \(j\), the extra rows are \(L\le a<j\). For any retained
physical row \(a\ge L\), and \(\Re x\le q_R\),
\[
 \frac12-\Re x-\frac{\tau_a}{2\pi}
                   \ge-\frac{R-L}{N}\ge-\varepsilon.
 \tag{29}
\]
If the ordinary row contour uses the midpoint cut
\(T_L=\pi-2\pi L/N\), the corresponding bound is
\[
 \frac12-\Re x-\frac{|\Re t|}{2\pi}
       \ge-\frac{R-L+1/2}{N}
       \ge-\varepsilon-\frac1{2N},
                   \qquad |\Re t|\le T_L.
 \tag{30}
\]
For \(L=0\), use the cut between the last physical angle and
\(\pi\) as before. Thus freezing support exchanges many
shared faces for a reflected factorial region of controlled
width. Taking one block with \(L=0\) recovers the original
global-support contour, rather than eliminating that region.

No estimate of the grouped block seams follows from (27).
Moreover, substituting
\(\mathscr D=h/Q-\mathcal I/Q\) in the block's reduced-pole
representation still produces both the original-density and
the interpolation-observation terms. A phase gap proved for
the original double-pole density does not bound the latter
terms. This is the remaining analytic cost of the exact
grouping.

## 7. The original density behind a frozen support

There are two exact ways to keep the frozen support without
estimating the two parts of \(\mathscr D=(h-\mathcal I)/Q\)
separately. One changes the wire polynomial; the other restores
an explicit original first-normal sum. Neither deletes that
sum or proves its exponential gap.

Write \(\mathcal H_a[f]=(4-c_a^2)f'(c_a)-c_af(c_a)\), and,
with the crossing scalar outside \(h=h_{n,N}\), define
\[
 \mathcal T_{n,E}[f]
   =\eta C_{N,n}\sum_{a\in E}\mathcal H_a[f]
   =\frac{\eta C_{N,n}N^2}{2\pi i}
                 \oint_{\Gamma_E}\frac{f(z)}{Q(z)^2}\,dz.
 \tag{31}
\]
Contours are positively oriented and enclose exactly the
specified nodes. The second equality holds for holomorphic
\(f\) there. Indeed
\((4-c_a^2)Q'(c_a)^2=N^2\) and
\(Q''(c_a)/Q'(c_a)=c_a/(4-c_a^2)\), so its double-pole
residue is precisely the first expression. In particular,
\(\mathcal T_{n,E}[hB]\) is the literal original retained
trace, not a value-only replacement.

For a fixed support \(L\), put
\[
 P_{L,x}(z)=\sum_{a=L}^{m-1}B_a(x)\ell_a(z),\qquad
 E_L=\{L,\ldots,m-1\}.
 \tag{32}
\]
This is an ordinary polynomial of degree less than \(m\).
It is divisible by \(\prod_{a<L}(z-c_a)\), and
\(P_{L,j/N}=e_j\) as polynomials for every \(L\le j<m\).

**Proposition 6.** The frozen coefficient has the exact
original-source representation
\[
 A_{n,L}(x)
   =\mathcal T_{n,\{0,\ldots,m-1\}}[hP_{L,x}]
   =\phi_N[R^n\mathcal L_NP_{L,x}].
 \tag{33}
\]
Let \(\Gamma_L\) surround the nodes in \(E_L\), and let
\(\Gamma_{\rm all}\) lie outside it and surround every node.
Choose both inside a domain of holomorphy of \(h\). Then
\[
 \begin{split}
 P_{L,x}(z)
   &=\frac{Q(z)}{2\pi i}\oint_{\Gamma_L}
        \frac{B(x,\zeta)}{Q(\zeta)(z-\zeta)}\,d\zeta,
                 &&z\text{ outside }\Gamma_L,\\
 A_{n,L}(x)
   &=\frac{\eta C_{N,n}N^2}{(2\pi i)^2}
       \oint_{\Gamma_{\rm all}}\oint_{\Gamma_L}
       \frac{h(z)B(x,\zeta)}
            {Q(z)Q(\zeta)(z-\zeta)}\,d\zeta\,dz .
 \end{split}
 \tag{34}
\]
Here \(B\) may always be \(P_x\). It may instead be the
factorial representative \(B_N(x,t)\), \(\zeta=-2\cos t\),
when that representative is holomorphic on and inside
\(\Gamma_L\). The formula uses its physical values only.

*Proof.* The normal-defect identity applied to the degree
less than \(m\) polynomial \(P_{L,x}\) gives (33) from (6).
Equivalently, the full interpolation term has zero trace:
\(\deg(\mathcal I_{n,N}P_{L,x})\le 2m-2=N-2\).
The first integral in (34) has residues
\(Q(z)B_a(x)/(Q'(c_a)(z-c_a))=B_a(x)\ell_a(z)\).
Substitution in (31) gives the second integral.
Conversely, integrate in \(z\) first. Its residues are
\[
 \frac{h(\zeta)}{Q(\zeta)}
       +\sum_{a=0}^{m-1}\frac{h(c_a)}{Q'(c_a)(c_a-\zeta)}
          =\frac{h(\zeta)-\mathcal I_{n,N}(\zeta)}
                  {Q(\zeta)}
          =\mathscr D_{n,N}(\zeta).
 \]
This recovers exactly (13) with support \(L\), including its
normalization. \(\square\)

Inserting the second line of (34), for \(n\) and \(p\),
in the single block integral (27) gives a nested five-variable
integral with scalar
\(C_{N,n}C_{N,p}N^4/(2\pi i)^5\), the wire factor \(k_N(x)\),
and the product of the two displayed Cauchy kernels.
There are no interpolation polynomials in its numerator.
This is an exact representation of the original block sum.
All physical endpoint nodes occur on their original side of
the support cut. All contours are closed: replacing an angle
contour by its folded lower side requires the vertical terms
of the [exact trace formula](research_exact_complete_trace_contour.md#3-removing-outer-grid-points),
not just its horizontal integral.

The Cauchy diagonal is essential. If \(z\) is moved inside
\(\Gamma_L\), the first line of (34) becomes
\[
 P_{L,x}(z)
   =B(x,z)+\frac{Q(z)}{2\pi i}\oint_{\Gamma_L}
          \frac{B(x,\zeta)}{Q(\zeta)(z-\zeta)}\,d\zeta.
 \tag{35}
\]
The residue at \(\zeta=z\) is \(-B(x,z)/Q(z)\).
Thus the original factorial factor reappears by an explicit
diagonal residue; keeping the defect unsplit does not remove
this contribution. These formulas can first be used with
ordinary polynomials, so no factorial pole is implicit in
them. When the factorial representative is used, its own
holomorphy domain must also be retained. Splitting a reflected
factor introduces the moving poles described in the
[reflected-current identity](research_internal_pair_reflected_current_identity.md);
their cancellation in the original unsplit factor is not
permission to discard residues of its split pieces.

There is also a version that keeps the factorial density and
uses only original physical values in the correction. Let
\(\widetilde B_N(x,z)=\sum_{j=0}^{N-1}s_N(x-j/N)e_j(z)\)
be the full cardinal representative from the
[finite-band theorem](research_newton_interpolation_finite_fourier_band.md).
It agrees with \(B_N\) in every physical value and first
normal. Define the entire functions
\[
 \begin{split}
 T_{n,L}(x)&=\mathcal T_{n,E_L}[h\widetilde B_N(x,\cdot)],\\
 R_{n,L}(x)&=\eta C_{N,n}
       \sum_{a<L}(4-c_a^2)h(c_a)
                       \partial_z\widetilde B_N(x,c_a).
 \end{split}
 \tag{36}
\]
Then the following is another exact form of the block sum:
\[
 \sum_{j=L}^{R}\widetilde W_{n,N}(j/N)\widetilde W_{p,N}(j/N)
  =\frac1{2\pi i}\oint_{\partial\Omega_{L,R}}k_N(x)
       [T_{n,L}(x)+R_{n,L}(x)]
       [T_{p,L}(x)+R_{p,L}(x)]\,dx.
 \tag{37}
\]
At every wire pole \(j/N\) in the block,
\(\widetilde B_N=e_j\) and \(e_j(c_a)=0\) for \(a<L\).
The omitted original trace therefore consists exactly of the
first-normal term in (36). This proves (37) by residues.
Every factor in (36) is entire in \(x\); the product in
(37) retains all four terms, including \(R_{n,L}R_{p,L}\).

For comparison, the direct split of (13) is
\[
 A_{n,L}
   =T_{n,L}-\mathcal T_{n,E_L}
                  [\mathcal I_{n,N}\widetilde B_N].
 \tag{38}
\]
With \(P_x\) instead of \(\widetilde B_N\), the full-node
interpolation trace is zero, and its retained part is the
negative omitted-node part. With \(\widetilde B_N\), the
full-node term is a pure high-wire cardinal sum: writing
\(\mathcal I_{n,N}=\sum_{r<m}\iota_r e_r\), it is
\(C_{N,n}\sum_{j=m}^{N-1}s_N(x-j/N)\iota_{N-1-j}\).
This uses the original pairing
\(\phi_N(e_r e_j)=\delta_{r+j,N-1}\).
It vanishes at every low wire node, but not at a general
complex \(x\). The omitted terms involving
\(\widetilde B_N(x,c_a)\) also vanish at the block nodes.
Consequently (38) reduces to (37) only after taking the
block residues, not as a pointwise deletion of its
interpolation term.

Equations (34) and (37) avoid a separately estimated
half-charge correction in two different exact ways.
The first requires control of the projected kernel and its
Cauchy diagonal. The second requires control of the original
omitted first-normal sums, coherently with the retained
trace. A horizontal phase bound for \(T_{n,L}T_{p,L}\)
alone does not establish either missing estimate.
These identities commute with ordinary derivatives in any
outside polynomial parameter. Their present scope is even
levels; the odd simple node and top-degree trace term require
their separate original corrections.

## 8. An exact kernel antiderivative and its amplification

The projected Cauchy transform does not have a polynomial operator
norm on bounded holomorphic inputs. The following calculation uses
its actual physical weights, rather than an arbitrary interpolation
matrix. It also supplies a discrete integration by parts for the
specified original defect.

Write \(X=\pi x\), \(\theta=\pi/N\), and define
\[
 g_a(x)=\frac{(-1)^a B_a(x)\sin(a\theta-X)\cos(a\theta)}
                         {\cos(X+\theta)}\quad(0\le a<m),
 \qquad g_m(x)=0.
 \tag{39}
\]
The apparent singularities are removable, as follows either from
the finite product (2) or from the identity below, starting at
\(a=m-1\). In particular every \(g_a\) is entire.

**Proposition 7.** The exact identities are
\[
 \begin{split}
 g_a-g_{a+1}&=(-1)^a\sin((2a+1)\theta)B_a,\\
 \sum_{a=L}^{m-1}\frac{f(c_a)B_a(x)}{Q'(c_a)}
   &=\frac2N\left\{f(c_L)g_L(x)
        +\sum_{a=L+1}^{m-1}[f(c_a)-f(c_{a-1})]g_a(x)\right\}.
 \end{split}
 \tag{40}
\]
The second identity holds for arbitrary assigned values \(f(c_a)\).
For the original defect it gives, without approximation,
\[
 A_{n,L}(x)=2\eta C_{N,n}N\left\{
     \mathscr D_{n,N}(c_L)g_L(x)
     +\sum_{a=L+1}^{m-1}
       [\mathscr D_{n,N}(c_a)-\mathscr D_{n,N}(c_{a-1})]g_a(x)
                                  \right\}.
 \tag{41}
\]

*Proof.* Formula (2) gives
\(B_{a+1}/B_a=\sin((a+1)\theta+X)/\sin((a+1)\theta-X)\).
The elementary identity
\[
 \sin(a\theta-X)\cos(a\theta)
 +\sin((a+1)\theta+X)\cos((a+1)\theta)
       =\sin((2a+1)\theta)\cos(X+\theta)
\]
proves the first line of (40). At the last row,
\(\sin((m-1)\theta-X)=\cos(X+\theta)\), so
\(g_{m-1}=(-1)^{m-1}\sin\theta\,B_{m-1}\); no artificial
last-row value is used. Finally
\(1/Q'(c_a)=2(-1)^a\sin((2a+1)\theta)/N\).
Summation by parts proves the second line and (41).
\(\square\)

For full support the boundary term is particularly small:
\[
 g_0(x)=-\frac{\sin(\pi Nx)}{N\cos(\pi x+\pi/N)},
 \qquad
 A_{n,0}(x)=
 -\frac{2\eta C_{N,n}\mathscr D_{n,N}(c_0)\sin(\pi Nx)}
        {\cos(\pi x+\pi/N)}
 +2\eta C_{N,n}N\sum_{a=1}^{m-1}
       [\mathscr D_{n,N}(c_a)-\mathscr D_{n,N}(c_{a-1})]g_a(x).
 \tag{42}
\]
At fixed nonzero \(\Im x\), the boundary factor
\(\sin(\pi Nx)/\cos(\pi x+\pi/N)\) has exponential rate
\(\pi|\Im x|\). It is only polynomially large on the thin
points \(x_y\) used below; no fixed-height contour gap follows
from this formula.
The difference sum remains; it has not been bounded by its
separate absolute terms.

To quantify the operator amplification, put
\[
 (\mathcal C_{L,N}f)(x)=
             \sum_{a=L}^{m-1}\frac{f(c_a)B_a(x)}{Q'(c_a)}.
\]
Take \(6\mid N\), \(L=N/3\), and
\(x_y=(L+1/2+iy)/N\), with \(1/10\le y\le1/5\).
Proposition 7 gives the exact constant-input comparison
\[
 \begin{split}
 (\mathcal C_{L,N}1)(x_y)&=2g_L(x_y)/N,\\
 (\mathcal C_{0,N}1)(x_y)
       &=-\frac{2\sin(\pi Nx_y)}
                    {N^2\cos(\pi x_y+\pi/N)}.
 \end{split}
 \tag{43}
\]
Uniformly in this interval of \(y\), the second line has modulus
bounded above and below by positive multiples of \(N^{-2}\).
The first has the exponential rate
\[
 \frac1N\log|\mathcal C_{L,N}1(x_y)|
       =c+O(\log N/N),\qquad
 c=J(2/3)-2J(1/3)>8/25.
 \tag{44}
\]
Indeed \(|B_L(x_y)|=\exp\{Nc+O(\log N)\}\) by the proved
two-sided product estimate (24)–(25), whereas
\(|\sin(L\theta-\pi x_y)|\asymp N^{-1}\),
\(\cos(L\theta)=1/2\), and
\(|\cos(\pi x_y+\pi/N)|\asymp1\).

Thus on any fixed neighborhood of the physical interval, where
the constant input has supremum norm one, the norm of this frozen
projection grows at least as \(\exp\{Nc-O(\log N)\}\).
If one uses only the available defect bound
\(|f_N|\le N^A e^{N\mu_3}\), the constant test input
\(f_N=N^{-2}e^{N\mathcal S_3}\) produces
\[
 \frac1N\log|N^2\mathcal C_{L,N}f_N(x_y)|^2
             \longrightarrow 2\mu_3+2c>137/50>13/5.
 \tag{45}
\]
This rules out a pair-rate upper bound obtained solely from that
holomorphic norm and a subexponential projection norm. The test
input is not the original complete-source defect. Equation (45)
is an operator obstruction, not a counterexample for the knot or
a claimed asymptotic for (41).
At the finite-algebra level the constant defect is realized simply
by \(h=Q\), whose ordinary value interpolant is zero. Thus the
amplification occurs in this original projection itself; the test
does not obey the specified complete-source preparation.

It also explains why the leading holomorphic packet cannot be
substituted on the strength of its relative error alone. An additive
constant \(N^{-3}e^{N\mathcal S_3}\) is permitted by a relative
\(O(N^{-1})\) packet with the nonzero rational leading profile,
including its fixed-order holomorphic bounds on a smaller
neighborhood. Its projected contribution still has the rate in
(45). This describes an allowed error under those bounds; it does
not assert that the actual source has that error.

There are exact higher vanishing moments at the wire nodes, but
they are the already known divided-difference structure. For
\(L\le j<m\),
\[
 (\mathcal C_{L,N}f)(j/N)
   =\frac{(-1)^j}{S_j^2}
        [c_j,c_{j+1},\ldots,c_{m-1}]f.
 \tag{46}
\]
It vanishes for every polynomial \(f\) of degree less than
\(m-j-1\). Indeed at a wire node \(B_a=e_j(c_a)\), and
\(e_j/Q=(-1)^j/(S_j^2Q_{j,N})\); the usual simple-pole
formula gives the displayed divided difference. This is the
existing reduced-node cancellation. Iterating discrete integration
by parts must respect these moments. They do not extend as the
same vanishing identities to complex \(x\), and fixed-order
holomorphic derivative bounds alone do not control their
growing-order remainder.

## 9. Reproduction

The [focused checker](../experiments/check_pair_regular_support_cells.py)
compares the interpolation with the original value-and-normal
trace, checks both finite-product forms and zero high indices,
and verifies the shifted Fourier sum and shared-face jumps.
It also integrates the two complete wire-cell contours and
their combined two-cell block directly at level four.
The frozen-support checks compare (33), (38), and the restored
normal rows in (37) with literal Newton polynomials and original
Hermite traces. Two direct Cauchy integrals verify the exterior
projector and its interior diagonal residue in (34)–(35).
The final checks verify the kernel antiderivative, its constant-input
projection, summation by parts for the actual normal-defect weights,
and the polynomial vanishing moments at the original wire nodes.
These are exact finite identities
checked at high precision, not evidence for an unproved
global exponential gap.

~~~sh
python3 experiments/check_pair_regular_support_cells.py
~~~

The [saved result](../repro/results/research-pair-regular-support-cells.json)
records the source hashes and all check counts.
