# The energy cost of removing an adjacent pair from a positive path

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The geometric comparison needed for the radical remainder can be
reduced to two explicit inequalities for the return at a single
vertex. This note gives that reduction and its exact constants.
No completed certificate for either full interval verification is
presently established in this research record. The universal
comparison in Section 4 is therefore conditional on the support
inequalities in Section 3. The small-height estimate and the
geometric continuation used here have written proofs.

## 1. The quantity to be bounded

Let \(\Gamma\) be a finite original path, with selected vertices
of integer powers \(n_v\ge3\) and at least one complete outside
endpoint. Retain every original edge. The minimum square energy
\(F_\Gamma(\lambda)\), its charge vector \(\lambda\), and its
normalization are those of
[the energy comparison](research_edge_cut_energy_comparison.md),
equations (6)--(9). A charge zero makes the corresponding vertex
complete; charge one is its original filling equation.

Choose an edge joining two selected vertices \(v,w\). Set their
charges to zero and keep the other charges equal to one. The
resulting energy is \(F_L+F_R\), the sum for the two pieces
obtained by removing that edge and making its endpoints complete.
The removed edge itself has zero energy. Write
\[
 \mathcal C(n,p)
   =F_\Gamma(\mathbf1)-F_L-F_R,
 \qquad n=n_v,\quad p=n_w.
 \tag{1}
\]
All other powers and all original edge constants are fixed in this
notation. Corollary 7 of the energy comparison proves
\[
                   \mathcal C(n,p)\le\mathcal C(3,3)
                         \qquad(n,p\ge3).
 \tag{2}
\]
This is a variational comparison by explicit feasible assignments.
It does not require monotonicity of the old vertices' geometric
coordinates.

Give the reference pair of powers three the same charge
\(\chi\in[0,1]\). The
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md)
supplies the unique positive stationary solution throughout this
interval. At an active vertex write
\(t_j=a_j-iH_j\), with \(0<a_j<\pi\) and \(H_j>0\).
It proves, independently of the length of the path,
\[
 H_j< B:=\frac{23}{20},\qquad
 \sinh H_j<\sqrt3\sin a_j.
 \tag{3}
\]
The derivative of the minimum is \(\partial F/\partial\lambda_j
=\pi H_j\). Consequently
\[
 \frac{\mathcal C(3,3)}{\pi}
        =\int_0^1\bigl(H_v(\chi)+H_w(\chi)\bigr)\,d\chi.
 \tag{4}
\]
This integral is over actual stationary solutions, including their
continuous limit at charge zero.

## 2. Two domains containing every neighboring cosine

For \(b\in[0,\pi]\) and \(h\in[0,B]\), put
\[
 c=\cos((b-ih)/2)
     =\cos(b/2)\cosh(h/2)+i\sin(b/2)\sinh(h/2).
\]
If \(h\le C\), this number belongs to the closed quarter ellipse
\[
 D_C=\left\{x+iy:x,y\ge0,\quad
       \frac{x^2}{\cosh^2(C/2)}+
       \frac{y^2}{\sinh^2(C/2)}\le1\right\}.
 \tag{5}
\]
Its boundary consists of the two axis segments and the ellipse arc.
The stronger angle-height bound in (3) puts it in
\[
 E_C=\left\{\cos((b-ih)/2):0\le b\le\pi,\quad
        0\le h\le\min\bigl(C,\operatorname{arsinh}
                                   (\sqrt3\sin b)\bigr)\right\}.
 \tag{6}
\]
For \(0<C\le B\), set
\(b_C=\arcsin(\sinh C/\sqrt3)\). The boundary of \(E_C\)
has four pieces: the real interval \([0,1]\); the image of
\(h=\operatorname{arsinh}(\sqrt3\sin b)\) for
\(b\in[0,b_C]\); the image of \(h=C\) for
\(b\in[b_C,\pi-b_C]\); and the corresponding curved image
for \(b\in[\pi-b_C,\pi]\). The cosine is injective on this
closed half-strip, so these pieces bound its image. Both domains
contain \(1\), the value at a complete neighbor, and \(0\),
which may pad an absent incidence of a terminal vertex.

Choose the endpoint of the pair with greater height and denote its
angle and height by \(a,H\). Its partner has height at most \(H\),
and its other neighbor, if present, has height at most \(B\).
Put \(A=\tan((a-iH)/2)\). The two returns therefore have the form
\[
 r_1=\operatorname{arsinh}(Ac_1),\qquad
 r_2=\operatorname{arsinh}(Ac_2),\qquad
 r_1+r_2=\frac32H+i\left(\frac32a-\pi\chi\right),
 \tag{7}
\]
where \(c_1\in D_B,c_2\in D_H\), or, more restrictively,
\(c_1\in E_B,c_2\in E_H\). The absent return is zero.
The inverse hyperbolic sine is the original branch with positive
real part and imaginary part in \((-\pi/2,\pi/2)\).

For a real slope \(s\le0\), define
\[
 L_s(r)=\Re r-s\Im r.
 \tag{8}
\]
The real part of \(Ac\) is positive in either domain's interior.
Hence \(L_s(\operatorname{arsinh}(Ac))\) is harmonic there and
continuous on its boundary. Its maximum is attained on the boundary
pieces just listed. Limits at their endpoints are included.

## 3. The two finite support tests

The first test is the following assertion on a closed rectangle:
for every \(a\in[0,\pi]\), \(H\in[1/1000,B]\), there is a
nonpositive rational slope \(s\) such that
\[
 \max_{c\in D_B}L_s(\operatorname{arsinh}(Ac))
 +\max_{c\in D_H}L_s(\operatorname{arsinh}(Ac))
 <\frac32H-s\left(\frac32a-\pi\frac{50H}{59}\right).
 \tag{9}
\]
If (9) holds, the exact equation (7) cannot hold with
\(\chi\le50H/59\): since \(s\le0\), its actual right-hand
side after applying \(L_s\) is at least the right-hand side of
(9). Thus (9), together with the
[proved small-height lemma](research_pair_activation_small_height.md),
implies
\[
                  \max(H_v,H_w)<\frac{59}{50}\chi
                              \quad(0<\chi\le1).
 \tag{10}
\]

The second test uses the smaller domains. For every
\(a\in[0,\pi]\), \(H\in[37/40,B]\), require a rational
\(s\le0\) with
\[
 \begin{split}
 &\max_{c\in E_B}L_s(\operatorname{arsinh}(Ac))
 +\max_{c\in E_H}L_s(\operatorname{arsinh}(Ac))\\
 &\hspace{15mm}<\frac32H-s\left(\frac32a-\pi\,
       \min\left\{1,\frac{40}{37}
                            \left(H-\frac{37}{200}\right)\right\}\right).
 \end{split}
 \tag{11}
\]
For \(\chi\ge4/5\), a violation of
\[
            \max(H_v,H_w)<\frac{37}{200}+\frac{37}{40}\chi
 \tag{12}
\]
has \(H\ge37/40\) and makes the upper bound on \(\chi\) in
(11) valid. Equation (7) then contradicts (11). Thus that test
implies (12) on \([4/5,1]\).

The [certificate generator](../experiments/certify_positive_pair_activation_height.py)
subdivides each parameter rectangle into rational boxes. For each
box it selects a rational slope and two rational support budgets.
Arb interval arithmetic verifies both budgets over every boundary
piece and verifies that their sum is strictly below the required
right-hand side. Numerical optimization proposes slopes only; no
sampled value is accepted as an upper bound. A result is saved only
after the complete rectangle has been covered.

The [separate verifier](../experiments/replay_positive_pair_activation_height.py)
uses the saved rational slopes and budgets, with no optimization
or imported generator code. It checks exact coverage with
multiplicity one and repeats every support bound at 160 bits.
The branch extraction used in both computations is
\[
 \begin{split}
 d_\pm&=\sqrt{x^2+(y\pm1)^2},\qquad z=x+iy,\quad x\ge0,\\
 \Re\operatorname{arsinh}z
     &=\operatorname{arcosh}\bigl((d_++d_-)/2\bigr),\\
 \Im\operatorname{arsinh}z
     &=\arcsin\bigl((d_+-d_-)/2\bigr).
 \end{split}
 \tag{13}
\]
These formulas include the continuous right-half-plane boundary
values; they avoid choosing branches by floating-point sampling.

## 4. The consequence if both support tests pass

**Proposition.** Assuming (9) and (11), every path in Section 1
and every adjacent selected pair with integer powers at least three
satisfy
\[
             0<\frac{\mathcal C(n,p)}{\pi}
                   <\frac{5811}{5000}<\frac{4G}{\pi}-\frac1{1000},
 \qquad
 G=\sum_{j=0}^\infty\frac{(-1)^j}{(2j+1)^2}.
 \tag{14}
\]

*Proof.* Use (10) up to charge \(4/5\), and (12) thereafter.
Equation (4) gives
\[
 \begin{split}
 \frac{\mathcal C(3,3)}{\pi}
 &<2\int_0^{4/5}\frac{59}{50}\chi\,d\chi
       +2\int_{4/5}^1
                      \left(\frac{37}{200}+\frac{37}{40}\chi\right)d\chi\\
 &=\frac{5811}{5000}.
 \end{split}
 \tag{15}
\]
The inequalities are strict on every compact interval of positive
charges. Equation (2) proves the upper bound for the other powers.
The derivative formula gives strict positivity directly for their
own charge path. Finally the eight-term alternating sum is a lower
bound for \(G\), and \(\pi<22/7\). Exact rational arithmetic gives
\[
 \frac{4G}{\pi}-\frac{5811}{5000}
 >\frac{4}{22/7}\sum_{j=0}^{7}\frac{(-1)^j}{(2j+1)^2}
                           -\frac{5811}{5000}
 =\frac{712208857}{637702065000}>\frac1{1000}.
 \tag{16}
\]
This proves (14). \(\square\)

For a matching \(\mathfrak m\) of selected edges, activate its
disjoint pairs successively from the configuration where their
charges are zero. The remaining zero vertices split the path into
components of the same class. Apply (14) in the component containing
the pair at each step. With \(T=V(\mathfrak m)\), this gives
\[
 M_\Gamma(\lambda^T)-M_\Gamma(\mathbf1)
       =\frac{F_\Gamma(\mathbf1)-F_\Gamma(\lambda^T)}{\pi}
       <|\mathfrak m|\,\frac{5811}{5000}.
 \tag{17}
\]
Here \(M_\Gamma\) is the real part of the stationary phase with
its original absolute normalization. The complete-edge rate is
\(4G/\pi\). Thus (17) supplies a uniform geometric rate gap of
more than \(|\mathfrak m|/1000\) for the radical matching.

To obtain a quantum remainder estimate from this comparison one
still needs the hypothesis of
[the radical contraction theorem](research_radical_path_sector_gap.md),
equation (4): a bound on the whole real boundary period of every
remaining source component at its geometric rate. When those
bounds hold, its equation (5) and (17) give
\[
 |\mathscr T_{\mathfrak m,N}|
       \le C_{\mathfrak m}N^{b_{\mathfrak m}}
          \exp\left\{N\left(M_\Gamma(\mathbf1)
                                  -\frac{|\mathfrak m|}{1000}\right)\right\}.
 \tag{18}
\]
No nonzero coefficient of the main geometric contribution follows
from this upper bound. That coefficient, and the whole-boundary
bounds for arbitrary connected short components, remain separate
questions about the original quantum sums.

## 5. Removing any set of selected edges

The same comparison controls more than matchings. This extension
is useful for the midpoint terms of the truncated edge difference
equation. It remains conditional on the two support tests (9) and
(11).

**Corollary.** Let \(F\) be any nonempty set of edges whose endpoints
are selected, and put \(S=V(F)\). Then
\[
 0<
 M_\Gamma(\lambda^S)-M_\Gamma(\mathbf1)
 =\frac{F_\Gamma(\mathbf1)-F_\Gamma(\lambda^S)}{\pi}
 <|F|\,\frac{5811}{5000}
 <|F|\left(M_\infty-\frac1{1000}\right).
 \tag{19}
\]
Here \(\lambda^S\) makes precisely the vertices in \(S\) complete,
and \(M_\infty=4G/\pi\) is the original complete-edge rate.

*Proof.* Each connected component of \(F\) is a run of \(k\ge1\)
edges and \(k+1\) vertices. Partition its vertices into consecutive
adjacent pairs, with one singleton left if necessary. This uses
\(\lceil(k+1)/2\rceil\le k\) blocks.

Start with all charges in \(S\) zero. Activate the blocks in any
fixed order. At a pair use Proposition (14); at a singleton use
the already-proved single-activation bound
\[
 \frac{F(\lambda_v=1)-F(\lambda_v=0)}{\pi}
                 <\frac{23}{20}<\frac{5811}{5000}.
 \tag{20}
\]
This is Lemma 10 of the
[energy comparison](research_edge_cut_energy_comparison.md).
At each step the still-zero vertices split the path into
components with complete ends. The component containing the next
block satisfies the hypotheses of that comparison; the other
components are unchanged. In particular, powers elsewhere in the
path need not be three. Summing the strict bounds over at most
\(|F|\) blocks proves the first upper bound in (19). The last
bound is (16). Positivity follows from the charge derivative.
\(\square\)

Delete the edges of \(F\), make their endpoints complete, and
let \(C\) denote the remaining path components. Retain every
uncut edge, including an edge between two vertices of \(S\).
If \(\mu_C\) is the complete-boundary rate of \(C\), the absolute
action identity gives
\[
 \sum_C\mu_C
     =M_\Gamma(\lambda^S)-|F|M_\infty
     <M_\Gamma(\mathbf1)-\frac{|F|}{1000}.
 \tag{21}
\]
Indeed, reinserting each deleted edge joins complete endpoints
and restores exactly one constant \(M_\infty\). Such an edge has
zero square energy but nonzero absolute phase; these two
normalizations must not be confused.

The [midpoint forcing reduction](research_radical_path_sector_gap.md#7-the-middle-newton-polynomials-on-the-whole-real-period)
uses (21) for arbitrary \(F\). Its quantum estimate still
requires whole-real-boundary upper bounds for the shorter
components \(C\). No assertion that every contour remainder has
that form is made.
